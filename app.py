
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utang.db'
db = SQLAlchemy(app)

# Example model
class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/', methods=['GET', 'POST'])
def index():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        if table_name:
            try:
                db.session.execute(text(f'DROP TABLE IF EXISTS "{table_name}"'))
                db.session.commit()
                flash(f'Table "{table_name}" dropped successfully.', 'danger')
            except Exception as e:
                flash(str(e), 'warning')
        return redirect(url_for('index'))
    return render_template('index.html', tables=tables)

@app.route('/drop-all-tables', methods=['POST'])
def drop_all_tables():
    db.drop_all()
    flash('All tables dropped successfully!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
