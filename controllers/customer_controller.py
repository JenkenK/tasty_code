from flask import Blueprint, Flask, redirect, render_template, request

from models.customer import Customer
import repositories.customer_repositories as customer_repositories

customers_blueprint = Blueprint("customers", __name__)

@customers_blueprint.route("/customers")
def customers():
    customers = customer_repositories.select_all()
    return render_template("/customers/index.html", customers = customers)

@customers_blueprint.route("/customers/<id>")
def show_customer(id):
    customer = customer_repositories.select(id)
    return render_template("customers/show.html", customer = customer)

