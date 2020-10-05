from flask import Blueprint, Flask, redirect, render_template, request

from models.food import Food

import repositories.order_repository as order_repository
import repositories.food_repository as food_repository

food_blueprint = Blueprint("food", __name__)


# INDEX
@food_blueprint.route('/foods')
def foods():
    foods = food_repository.select_all()
    return render_template("foods/index.html", foods = foods)


# NEW
@food_blueprint.route('/foods/new', methods=['GET'])
def new_food():
    return render_template("/foods/new.html")

