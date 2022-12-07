# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/02 14:19:01 by marvin            #+#    #+#              #
#    Updated: 2022/12/02 14:19:01 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, redirect, url_for, render_template, request, flash, abort
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm

db = SQLAlchemy()


def application():

	class Todo(db.Model):
		__tablename__ = 'todo'
		id = db.Column(db.Integer, primary_key=True)
		name = db.Column(db.String(250), nullable=False)
		Ongoing = db.Column(db.Boolean(), nullable=False)
		pass

	class User(UserMixin):
		__tablename__ = "users"
		id = db.Column(db.Integer, primary_key=True)
		email = db.Column(db.String(100), unique=True)
		password = db.Column(db.String(100))
		name = db.Column(db.String(100))
		pass		


	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	bootstrap = Bootstrap(app)
	db.init_app(app)
	from views import todo_app
	app.register_blueprint(todo_app)
	login_manager = LoginManager()
	LoginManager.init_app(app)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	"""def admin_only(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			if current_user.id != 1:
				return abort(403)
			return f(*args, **kwargs)
		return decorated_function
"""

	@app.route('/register', methods=['GET', 'POST'])
	def about():
		form = RegisterForm()
		if form.validate_on_submit():
			if User.query.filter_by(email=form.email.data).first():
				flash("You have already registered with this email, log in instead")
				return redirect(url_for('index'))

			hash_and_salted_password = generate_password_hash(
	            form.password.data,
	            method='pbkdf2:sha256',
	            salt_length=8
	        )
			new_user = User(
	            email=form.email.data,
	            name=form.name.data,
	            password=hash_and_salted_password,
	        )
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			return redirect(url_for('index'))
		return render_template('register.html', form=form, current_user=current_user)

		@app.route('/')
		def index():
			return render_template("index.html")
		return app

if '__main__' == __name__:
	app = application()
	app.run(debug=True)