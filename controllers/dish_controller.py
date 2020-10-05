from flask import Blueprint, Flask, redirect, render_template, request

from models.dish import Dish

import repositories.dish_repository as dish_repository

dish_blueprint = Blueprint("dish", __name__)


# INDEX
@dish_blueprint.route('/dishes')
def dishes():
    dishes = dish_repository.select_all()
    return render_template("dishes/index.html", dishes = dishes)


# NEW
@dish_blueprint.route('/dishes/new', methods=['GET'])
def new_dish():
    return render_template("dishes/new.html")


# CREATE
@dish_blueprint.route("/dishes", methods=["POST"])
def create_dish():
    pass