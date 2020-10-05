from flask import Blueprint, Flask, redirect, render_template, request

from models.food import Food

import repositories.order_repository as order_repository
import repositories.dish_repository as dish_repository

dish_blueprint = Blueprint("dish", __name__)


# INDEX
@food_blueprint.route('/foods')
def foods():
    foods = food_repository.select_all()
    return render_template("foods/index.html", foods = foods)


# NEW
@food_blueprint.route('/foods/new', methods=['GET'])
def new_dish():
    return render_template("/foods/new.html")


# CREATE
@food_blueprint.route("/foods", methods=["POST"])
def create_dish():
    food = request.form['cui']
    new_cuisine = Cuisine(cuisine)
    cuisine_repository.save(new_cuisine)
    return redirect("/cuisines")