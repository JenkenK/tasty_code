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


# CREATE
@customers_blueprint.route("/customers", methods=["POST"])
def create_customer():
    name = request.form['name']
    address = request.form['address']
    payment = request.form['payment']
    phone_number = request.form['phone_number']
    service = request.form['service']

    new_customer = Customer(name, address, payment, phone_number, service)

    customer_repository.save(new_customer)
    return redirect('/customers')


# EDIT
@customers_blueprint.route("/customers/<id>/edit")
def edit_customer(id):
    customer = customer_repository.select(id)
    return render_template('customers/edit.html', customer = customer)


# UPDATE
@customers_blueprint.route("/customers/<id>", methods=['POST'])
def update_customer(id):
    name = request.form['name']
    address = request.form['address']
    payment = request.form['payment']
    phone_number = request.form['phone_number']
    service = request.form['service']

    update_customer = Customer(name, address, payment, phone_number, service, id)
    customer_repository.update(update_customer)
    return redirect("/customers")
 

# DELETE
@customers_blueprint.route("/customers/<id>/delete", methods=['POST'])
def delete_customer(id):
    customer_repository.delete(id)
    return redirect("/customers")
