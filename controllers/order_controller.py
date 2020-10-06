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
    customer_id = request.form['customer']
    restaurant_id = request.form['restaurant']

    customer = customer_repository.select(customer_id)
    restaurant = restaurant_repository.select(restaurant_id)

    new_order = Order(order_timestamp, customer, restaurant)

    order_repository.save(new_order)
    return redirect('/orders')


# EDIT
@order_blueprint.route('/orders/<order_id>/edit')
def edit_order(order_id):
    order = order_repository.select(order_id)
    restaurants = restaurant_repository.select_all()
    customers = customer_repository.select_all()
    return render_template('orders/edit.html', order=order, restaurants=restaurants, customers=customers)
    

# UPDATE
@order_blueprint.route("/orders/<order_id>", methods=['POST'])
def update_order(order_id):
    timestamp = request.form["order_timestamp"]
    customer_id = request.form["customer"]
    restaurant_id = request.form["restaurant"]

    customer = customer_repository.select(customer_id)    
    restaurant = restaurant_repository.select(restaurant_id)

    update_order = Order(timestamp, customer, restaurant, order_id)
    order_repository.update(update_order)
    return redirect("/orders")


# DELETE
@order_blueprint.route('/orders/<order_id>/delete', methods=['POST'])
def delete_order(order_id):
    order_repository.delete(order_id)
    return redirect('/orders')
