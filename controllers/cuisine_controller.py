from flask import Blueprint, Flask, redirect, render_template, request

from models.cuisine import Cuisine
import repositories.cuisine_repository as cuisine_repository

cuisine_blueprint = Blueprint("cuisine", __name__)

# INDEX
@cuisine_blueprint.route("/cuisines")
def cuisine():
    cuisines = cuisine_repository.select_all()
    return render_template("cuisines/index.html", cuisines=cuisines)


# NEW
@cuisine_blueprint.route("/cuisines/new")
def new_cuisine():
    return render_template("cuisines/new.html")


# CREATE
@cuisine_blueprint.route("/cuisines", methods=["POST"])
def create_cuisines():
    cuisine = request.form['cuisine']
    new_cuisine = Cuisine(cuisine)
    cuisine_repository.save(new_cuisine)
    return redirect("/cuisines")


# EDIT
@cuisine_blueprint.route("/cuisines/<id>/edit")
def edit_cuisines(id):
    cuisine = cuisine_repository.select(id)
    return render_template('cuisines/edit.html', cuisine=cuisine)


# UPDATE
@cuisine_blueprint.route("/cuisines/<id>", methods=['POST'])
def update_cuisines(id):
    cuisine = request.form["cuisine"]
    update_cuisine = Cuisine(cuisine, id)
    cuisine_repository.update(update_cuisine)
    return redirect("/cuisines")


# DELETE
@cuisine_blueprint.route("/cuisines/<id>/delete", methods=['POST'])
def delete_cuisine(id):
    cuisine_repository.delete(id)
    return redirect("/cuisines")