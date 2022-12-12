from flask import Blueprint, flash, redirect, render_template, url_for
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User
from flask_login import login_required, login_user, logout_user, current_user

auth =  Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		if User.query.filter_by(email=form.email.data).first():
			flash("You have already registered with this email, log in instead")
			return redirect(url_for('todo_app.index'))

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
		return redirect(url_for('todo_app.main'))
	return render_template('register.html', form=form, user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('todo_app.main'))
			else:
				flash('Incorrect Password, please try again.', category='error')
		else:
			flash(message='Email doesnt exist.', category='error')
	return render_template('login.html', user=current_user, form=form)

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
	logout_user()
	return redirect(url_for('todo_app.index'))