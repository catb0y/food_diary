#!/usr/bin/python
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import os
import json
import pygal
import jsonpickle

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
    labels = Meal.query.all()

    values = labels # can you iterate through a query? here or in html



    return render_template('index.html', labels=labels, values=values)


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


@app.route('/archive')
def archive():
    meals = Meal.query.all()
    return render_template('archive.html', meals=meals)





if __name__== '__main__':
    app.run(debug=True)



# Todo Breakdown
# create chart
    # how to jsonify my classes? // how to get code in JS jinja2?
    # how to turn my jsonized content into chart (in JS?)?
