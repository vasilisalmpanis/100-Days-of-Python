from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL

class CreateCafe(FlaskForm):
	name = StringField("Name", validators=[DataRequired(message='Please specify a name')])
	map_url = StringField("Map Url", validators=[DataRequired(), URL(message="Please provide a working url")])
	img_url = StringField("Img Url", validators=[DataRequired(), URL(message="Please provide a working url")])
	location = StringField("Location", validators=[DataRequired(message='Please specify a location')])
	has_wifi = BooleanField("Wifi")
	has_toilet = BooleanField("Toilet")
	has_socket = BooleanField("Socket")
	can_take_calls = BooleanField("Calls")
	seats = StringField("Seats", validators=[DataRequired(message='Please specify the number of seats')])
	coffee_price = StringField("Coffee Price", validators=[DataRequired(message='Please specify the coffee price')])
	submit = SubmitField("Submit Cafe")