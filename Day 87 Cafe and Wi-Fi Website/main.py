from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafe-website.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)

with app.app_context():
	db.create_all()

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/add_secret', methods=['GET', 'POST'])
def add():




if '__main__' == __name__:
	app.run(debug=True)





