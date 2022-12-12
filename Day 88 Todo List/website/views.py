from flask import redirect, url_for, render_template, flash, Blueprint
from flask_login import login_user, current_user, login_required
from .models import Todo
from . import db
from .forms import RegisterForm, LoginForm, NewTodo
from werkzeug.security import generate_password_hash

todo_app = Blueprint('todo_app', __name__)


@todo_app.route('/', methods=['GET'])
def index():
	return render_template('index.html', user=current_user)

@todo_app.route('/about', methods=['GET'])
def about():
	return render_template('about.html', user=current_user)

@todo_app.route("/main", methods=['GET', 'POST'])
@login_required
def main():
	todos = Todo.query.all()
	return render_template("main.html", user=current_user, todos=todos)

@todo_app.route("/new_todo", methods=['GET', 'POST'])
@login_required
def add():
	form = NewTodo()
	if form.validate_on_submit():
		new_todo = Todo(
			name = form.Name.data,
			Ongoing = True,
			user_id = current_user.id,
		)
		db.session.add(new_todo)
		db.session.commit()
		return redirect(url_for('todo_app.main',))
	return render_template("new_todo.html", user=current_user, form=form)

@todo_app.route("/delete/<int:todo_id>")
def delete_post(todo_id):
    post_to_delete = Todo.query.get(todo_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('todo_app.main'))