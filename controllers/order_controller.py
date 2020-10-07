from flask import Blueprint, Flask, redirect, render_template, request

from models.order import Order
from models.order_dish import OrderDish

import repositories.order_repository as order_repository
import repositories.customer_repository as customer_repository
import repositories.restaurant_repository as restaurant_repository
import repositories.dish_repository as dish_repository
import repositories.order_dish_repository as order_dish_repository

order_blueprint = Blueprint("order", __name__)


# INDEX
@order_blueprint.route('/orders')
def orders():
    orders = order_repository.select_all()
    order_dishes = order_dish_repository.select_all()
    return render_template("/orders/index.html", orders = orders, order_dishes = order_dishes)


# NEW
@order_blueprint.route('/orders/new', methods=['GET'])
def new_order():
    orders = order_repository.select_all()
    customers = customer_repository.select_all()
    restaurants = restaurant_repository.select_all()
    dishes = dish_repository.select_all()
    return render_template("/orders/new.html", orders = orders, customers = customers, restaurants = restaurants, dishes = dishes)


# CREATE
@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    order_timestamp = request.form['order_timestamp']
    customer_id = request.form['customer']
    restaurant_id = request.form['restaurant']
    dish_ids = request.form.getlist('dishes')

    customer = customer_repository.select(customer_id)
    restaurant = restaurant_repository.select(restaurant_id)

    new_order = Order(order_timestamp, customer, restaurant)
    order_repository.save(new_order)

    order_dishes = []
    for id in dish_ids:
        new_order_dish = OrderDish(new_order, dish_repository.select(id))
        order_dish_repository.save(new_order_dish)
        order_dishes.append(new_order_dish)

    return redirect('/orders')


# EDIT
@order_blueprint.route('/orders/<order_id>/edit')
def edit_order(order_id):
    order = order_repository.select(order_id)
    restaurants = restaurant_repository.select_all()
    customers = customer_repository.select_all()
    dishes = dish_repository.select_all()
    order_dishes = order_dish_repository.select_all()
    return render_template('orders/edit.html', order=order, restaurants=restaurants, customers=customers, dishes = dishes, order_dishes = order_dishes)
    

# UPDATE
@order_blueprint.route("/orders/<order_id>", methods=['POST'])
def update_order(order_id):
    timestamp = request.form["order_timestamp"]
    customer_id = request.form["customer"]
    restaurant_id = request.form["restaurant"]
    dish_ids = request.form.getlist('dishes')

    customer = customer_repository.select(customer_id)    
    restaurant = restaurant_repository.select(restaurant_id)

    update_order = Order(timestamp, customer, restaurant, order_id)
    order_repository.update(update_order)

    updated_order_dishes = []
    for id in dish_ids:
        updated_order_dish = OrderDish(update_order, dish_repository.select(id))
        order_dish_repository.save(updated_order_dish)
        updated_order_dishes.append(updated_order_dishes)

    return redirect("/orders")


# DELETE
@order_blueprint.route('/orders/<order_id>/delete', methods=['POST'])
def delete_order(order_id):
    order_dish_repository.delete(order_id)
    order_repository.delete(order_id)
    return redirect('/orders')
