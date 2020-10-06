from flask import Blueprint, Flask, redirect, render_template, request

from models.order_dish import OrderDish

import repositories.order_dish_repository as order_dish_repository
import repositories.dish_repository as dish_repository

order_dish_blueprint = Blueprint("order_dish", __name__)