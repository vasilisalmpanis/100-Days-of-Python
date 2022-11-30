from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from forms import CreateCafe
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafe-website.db"
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Cafe(db.Model):
	__tablename__ = 'cafe'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250), nullable=False)
	map_url= db.Column(db.String(500), nullable=False)
	img_url= db.Column(db.String(500), nullable=False)
	location = db.Column(db.String(250), nullable=False)
	has_toilet = db.Column(db.Boolean(), nullable=False)
	has_wifi = db.Column(db.Boolean(), nullable=False)
	has_sockets = db.Column(db.Boolean(), nullable=False)
	can_take_calls = db.Column(db.Boolean(), nullable=False)
	seats = db.Column(db.String(250), nullable=False)
	coffee_price = db.Column(db.String(250), nullable=False)
	pass

#with app.app_context():
#db.create_all()



@app.route('/', methods=['GET'])
def index():
	cafes = Cafe.query.all()
	header = ['Name', 'Map', 'Img', 'Location','Toilet', 'Wi-Fi', 'Socket','Calls', 'Seats', 'Coffee Price']
	return render_template('index.html', all_cafes = cafes, headers=header)

@app.route('/add_page', methods=['GET', 'POST'])
def add():
	form = CreateCafe()
	if form.validate_on_submit():
		if Cafe.query.filter_by(name=form.name.data).first():
			# User already exists
			error = 'Error, Cade already exists'
			flash("Cafe already exists, please try a different one")
			return redirect(url_for('add'))
		new_post = Cafe(
			name = form.name.data,
			img_url=form.img_url.data,
			map_url=form.map_url.data,
			location=form.location.data,
			has_wifi=form.has_wifi.data,
			has_toilet=form.has_toilet.data,
			has_sockets=form.has_socket.data,
			can_take_calls=form.can_take_calls.data,
			seats = form.seats.data,
			coffee_price = form.coffee_price.data
		)
		db.session.add(new_post)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("new-cafe.html", form=form)

@app.route('/modify', methods=['GET'])
def modify():
	cafes = Cafe.query.all()
	header = ['Name', 'Delete']
	render_template("modify_cafes.html", all_cafes=cafes)

@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    post_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('index'))


if '__main__' == __name__:
	app.run(debug=True)

