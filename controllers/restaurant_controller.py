from flask import Blueprint, Flask, redirect, render_template, request

from models.restaurant import Restaurant
import repositories.restaurant_repository as restaurant_repository
import repositories.cuisine_repository as cuisine_repository
import repositories.customer_repository as customer_repository

restaurant_blueprint = Blueprint("restaurant", __name__)


#INDEX
@restaurant_blueprint.route("/restaurant")
def restaurants():
    restaurants = restaurant_repository.select_all()
    return render_template("/restaurant/index.html", restaurants = restaurants)
    