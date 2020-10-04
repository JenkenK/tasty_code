from flask import Blueprint, Flask, redirect, render_template, request

from models.restaurant import Restaurant
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

    