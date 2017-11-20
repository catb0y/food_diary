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
    

# Views
@app.route('/')
@app.route('/index')
def main():
    render_template('index.html')
