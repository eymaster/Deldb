
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utang.db'
db = SQLAlchemy(app)

# Example model (you can delete this)
class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drop-tables', methods=['POST'])
def drop_tables():
    db.drop_all()
    flash('All tables dropped successfully!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
