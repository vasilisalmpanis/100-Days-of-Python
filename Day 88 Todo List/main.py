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

from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

db = SQLAlchemy()


def application():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	bootstrap = Bootstrap(app)
	db.init_app(app)
	from views import todo_app
	app.register_blueprint(todo_app)

	@app.route('/')
	def index():
		return render_template("index.html")

	return app

if '__main__' == __name__:
	app = application()
	app.run(debug=True)