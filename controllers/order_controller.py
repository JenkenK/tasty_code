from flask import Blueprint, Flask, redirect, render_template, request

from models.order import Order

import repositories.order_repository as order_repository
import repositories.customer_repository as customer_repository
import repositories.restaurant_repository as restaurant_repository

order_blueprint = Blueprint("order", __name__)


# INDEX
@order_blueprint.route('/orders')
def orders():
    orders = order_repository.select_all()
    return render_template("/orders/index.html", orders = orders)


# NEW
@order_blueprint.route('/orders/new', methods=['GET'])
def new_order():
    orders = order_repository.select_all()
    customers = customer_repository.select_all()
    restaurants = restaurant_repository.select_all()
    return render_template("/orders/new.html", orders = orders, customers = customers, restaurants = restaurants)


# CREATE
@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    order_timestamp = request.form['order_timestamp']
    customer_id = request.form['customer_id']
    restaurant_id = request.form['restaurant_id']

    new_order = Order(order_timestamp, customer_id, restaurant_id)

    order_repository.save(new_order)
    return redirect('/orders')


# EDIT