from flask import Blueprint, Flask, redirect, render_template, request

from models.restaurant import Restaurant
from models.cuisine import Cuisine
import repositories.restaurant_repository as restaurant_repository
import repositories.cuisine_repository as cuisine_repository
import repositories.customer_repository as customer_repository

restaurant_blueprint = Blueprint("restaurant", __name__)


# INDEX
@restaurant_blueprint.route("/restaurants")
def restaurants():
    restaurants = restaurant_repository.select_all()
    return render_template("/restaurants/index.html", restaurants = restaurants)


# NEW
@restaurant_blueprint.route("/restaurants/new", methods=['GET'])
def new_restaurant():
    cuisines = cuisine_repository.select_all()
    return render_template("/restaurants/new.html", cuisines = cuisines)


# CREATE
@restaurant_blueprint.route("/restaurants", methods=['POST'])
def create_restaurant():
    name = request.form['name']
    cuisine_id = request.form['cuisine_id']
    address = request.form['address']
    phone_number = request.form['phone_number']
    availability = request.form['availability']

    new_restaurant = Restaurant(name, address, phone_number, availability, cuisine_id)

    restaurant_repository.save(new_restaurant)
    return redirect('/restaurants')


# EDIT
@restaurant_blueprint.route("/restaurants/<restaurant_id>/edit")
def edit_restaurant(restaurant_id):
    restaurant = restaurant_repository.select(restaurant_id)
    cuisines = cuisine_repository.select_all()
    return render_template('restaurants/edit.html', restaurant=restaurant, cuisines=cuisines)


# UPDATE
@restaurant_blueprint.route("/restaurants/<restaurant_id>", methods=['POST'])
def update_restaurant(restaurant_id):
    restaurant = request.form["restaurant"]
    cuisine_id = request.form["cuisine_id"]
    address = request.form["address"]
    phone_number = request.form["phone_number"]
    availability = request.form["availability"]

    update_restaurant = Restaurant(restaurant, address, phone_number, availability, cuisine_id, restaurant_id)
    restaurant_repository.update(update_restaurant)
    return redirect("/restaurants")


# DELETE
@restaurant_blueprint.route('/restaurants/<id>/delete', methods=['POST'])
def delete_restuarant(id):
    restaurant_repository.delete(id)
    return redirect('/restaurants')
