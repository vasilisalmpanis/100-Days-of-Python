from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafe-website.db"
	app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
	bootstrap = Bootstrap(app)
	db.init_app(app)

	from views import cafe_app
	app.register_blueprint(cafe_app)

	@app.route('/')
	def index():
		return render_template("index.html")

	return app

if '__main__' == __name__:
	app = create_app()
	app.run(debug=True)

