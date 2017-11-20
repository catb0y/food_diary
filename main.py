#!/usr/bin/python
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "whatever floats your boat"

# SQLAlchemy object
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


# Models
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.Text)
    discomfort = db.Column(db.String(60))



# Views
@app.route('/')
@app.route('/index')
def main():
    if request.method == 'POST':
        food = request.form['food']
        discomfort = request.form['discomfort']

        meal = Meal(food=food, discomfort=discomfort)
        db.session.add(meal)
        db.session.commit()
        flash("Got it!")
        return redirect(url_for('main'))

    return render_template('index.html')


@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        food = request.form['food']
        discomfort = request.form['discomfort']

        meal = Meal(food=food, discomfort=discomfort)
        db.session.add(meal)
        db.session.commit()
        flash("Got it!")
        return redirect(url_for('main'))

    return render_template('add.html')








if __name__== '__main__':
    app.run(debug=True)
