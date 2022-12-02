from flask import Flask, redirect, url_for, render_template, request, flash, Blueprint
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from models import
from forms import

todo_app = Blueprint('todo_app', __name__)

@todo_app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

