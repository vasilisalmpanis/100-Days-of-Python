from main import db


class Cafe(db.Model):
	__tablename__ = 'cafe-websites'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	location = db.Column(db.String(250), nullable=False)
	cafe = db.Column(db.Boolean(), nullable=False)
	power = db.Column(db.Boolean(), nullable=False)
	pass