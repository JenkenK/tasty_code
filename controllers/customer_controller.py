from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repository as customer_repository

customers_blueprint = Blueprint("customers", __name__)


# INDEX
@customers_blueprint.route("/customers")
def customers():
    customers = customer_repository.select_all()
    return render_template("/customers/index.html", customers = customers)


# SHOW
@customers_blueprint.route("/customers/<id>")
def show_customer(id):
    customer = customer_repository.select(id)
    return render_template("customers/show.html", customer = customer)


# NEW
@customers_blueprint.route('/customers/new', methods=['GET'])
def new_customer():
    customers = customer_repository.select_all()
    return render_template("customers/new.html", customers = customers)


