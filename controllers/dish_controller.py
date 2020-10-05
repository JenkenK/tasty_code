from flask import Blueprint, Flask, redirect, render_template, request

from models.dish import Dish

import repositories.dish_repository as dish_repository
import repositories.restaurant_repository as restaurant_repository

dish_blueprint = Blueprint("dish", __name__)


# INDEX
@dish_blueprint.route('/dishes')
def dishes():
    dishes = dish_repository.select_all()
    return render_template("dishes/index.html", dishes = dishes)


# NEW
@dish_blueprint.route('/dishes/new', methods=['GET'])
def new_dish():
    restaurants = restaurant_repository.select_all()
    return render_template("dishes/new.html", restaurants = restaurants)


# CREATE
@dish_blueprint.route("/dishes", methods=["POST"])
def create_dish():
    name = request.form["name"]
    price = request.form["price"]
    description = request.form["description"]
    restaurant_id = request.form['restaurant']

    restaurant = restaurant_repository.select(restaurant_id)

    new_dish = Dish(name, price, description, restaurant)

    dish_repository.save(new_dish)
    return redirect('/dishes')



# EDIT
@dish_blueprint.route("/dishes/<id>/edit")
def edit_dish(id):
    dish = dish_repository.select(id)
    return render_template('dishes/edit.html', dish = dish)


# UPDATE
@dish_blueprint.route("/dishes/<id>", methods=['POST'])
def update_dish(id):
    name = request.form["name"]
    price = request.form["price"]
    description = request.form["description"]
    restaurant_id = request.form["restaurant"]

    restaurant = restaurant_repository.select(restaurant_id)

    update_dish = Dish(name, price, description, restaurant, id)
    dish_repository.update(update_dish)
    return redirect("/dishes")
 

# DELETE
@dish_blueprint.route("/dishes/<id>/delete", methods=['POST'])
def delete_dish(id):
    dish_repository.delete(id)
    return redirect("/dishes")