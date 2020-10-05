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
    update_dish = Dish(cuisine, id)
    dish_repository.update(update_dish)
    return redirect("/dishes")


# DELETE
@dish_blueprint.route("/dishes/<id>/delete", methods=['POST'])
def delete_dish(id):
    dish_repository.delete(id)
    return redirect("/dishes")