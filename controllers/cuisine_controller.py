from flask import Blueprint, Flask, redirect, render_template, request

from models.cuisine import Cuisine
import repositories.cuisine_repositories as cuisine_repositories

cuisine_blueprint = Blueprint("cuisine", __name__)

# INDEX
@cuisine_blueprint.route("/cuisines")
def cuisine():
    cuisines = cuisine_repositories.select_all()
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
    cuisine_repositories.save(new_cuisine)
    return redirect("/cuisines")


# EDIT
@cuisine_blueprint.route("/cuisines/<id>/edit")
def edit_cuisines(id):
    cuisine = cuisine_repositories.select(id)
    return render_template('cuisines/edit.html', cuisine=cuisine)


# UPDATE
@cuisine_blueprint.route("/cuisines/<id>", methods=['POST'])
def update_cuisines(id):
    cuisine = request.form["cuisine"]
    update_cuisine = Cuisine(cuisine, id)
    cuisine_repositories.update(update_cuisine)
    return redirect("/cuisines")


# DELETE
@cuisine_blueprint.route("/cuisines/<id>/delete", methods=['POST'])
def delete_cuisine(id):
    cuisine_repositories.delete(id)
    return redirect("/cuisines")