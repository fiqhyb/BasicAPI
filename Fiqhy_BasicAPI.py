from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    dob = db.Column(db.String(120))
    age = db.Column(db.Integer)

def __init__(self, name, email, dob, age):
    self.name = name
    self.email = email
    self.dob = dob
    self.age = age

@app.route('/')
def show_all():
    return render_template('show_all.html', users = users.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['dob'] or not request.form['age']:
            flash('Please enter all the fields', 'error')
        else:
            user = users(
                name=request.form['name'],
                email=request.form['email'],
                dob=request.form['dob'],
                age=request.form['age'])
            db.session.add(user)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True, port=8080)