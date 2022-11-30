from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Cafe(db.Model):
	__tablename__ = 'cafe-websites'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	location = db.Column(db.String(250), nullable=False)
	#wifi = db.Column(db.String(250), nullable=False)
	#power = db.Column(db.String(250), nullable=False)