from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
DB_NAME = "database.db"

def application():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	db.init_app(app)
	bootstrap = Bootstrap(app)

	from .views import todo_app
	from .auth import auth

	app.register_blueprint(todo_app)
	app.register_blueprint(auth)

	from .models import User, Todo


	with app.app_context():
		db.create_all()
		print('Created Database!')

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))



	return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')