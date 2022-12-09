from flask import redirect, url_for, render_template, flash, Blueprint
from flask_login import login_user, current_user
from .models import Todo
from . import db
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash

todo_app = Blueprint('todo_app', __name__)


@todo_app.route('/', methods=['GET'])
def index():
	return render_template('index.html', user=current_user)

@todo_app.route('/about', methods=['GET'])
def about():
	return render_template('about.html', user=current_user)

