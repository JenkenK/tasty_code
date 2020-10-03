from flask import Blueprint, Flask, redirect, render_template, request

from models.restaurant_category import RestaurantCategory
import repositories.restaurant_category_repo as restaurant_category_repo

restaurant_category_blueprint = Blueprint("restaurant_category", __name__)

@restaurant_category_blueprint.route("/restaurant_category")
def restaurant_category():
    restaurant_category = restaurant_category_repo.select_all()
    return render_template("restaurant_category/index.html", restaurant_category=restaurant_category)

@restaurant_category_blueprint.route("/restaurant_category/new")
def new_restaurant_category():
    return render_template("restaurant_category/new.html")


    
