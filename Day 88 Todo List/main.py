from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form

db = SQLAlchemy()


def application():
	app = Flask(__name__)
	bootstrap = Bootstrap(app)


	@app.route('/')
	def index():
		return render_template("index.html")

	return app

if '__main__' == __name__:
	app = application()
	app.run(debug=True)