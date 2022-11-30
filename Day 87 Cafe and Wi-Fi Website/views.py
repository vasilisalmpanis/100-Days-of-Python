from flask import Flask, redirect, url_for, render_template, request, flash, Blueprint
from forms import CreateCafe
from flask_bootstrap import Bootstrap
from main import db
from database import Cafe

cafe_app = Blueprint('cafe_app', __name__)

@cafe_app.route('/', methods=['GET'])
def index():
	cafes = Cafe.query.all()
	header = ['Name', 'Google Maps', 'Image', 'Location','Toilet', 'Wi-Fi', 'Socket','Calls', 'Seats', 'Coffee Price']
	return render_template('index.html', all_cafes = cafes, headers=header)
@cafe_app.route('/add_page', methods=['GET', 'POST'])
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
@cafe_app.route('/modify', methods=['GET'])
def modify():
	cafes = Cafe.query.all()
	header = ['Name', 'Delete']
	return render_template("modify_cafes.html", all_cafes=cafes, headers=header)
@cafe_app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    cafe_to_delete = Cafe.query.get_or_404(cafe_id)
    try:
        db.session.delete(cafe_to_delete)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    return redirect(url_for('cafe_app.modify'))