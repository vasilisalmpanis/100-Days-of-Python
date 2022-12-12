from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, URL


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register!")

class LoginForm(FlaskForm):
    email = StringField("Your Email", validators=[DataRequired()])
    password = PasswordField("Your Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")

class NewTodo(FlaskForm):
    Name = StringField("Describe your activity briefly", validators=[DataRequired()])
    submit = SubmitField("Add")