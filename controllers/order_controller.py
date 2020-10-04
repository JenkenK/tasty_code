from flask import Blueprint, Flask, redirect, render_template, request

from models.order import Order

import repositories.order_repository as order_repository

order_blueprint = Blueprint("order", __name__)


# INDEX
@order_blueprint.route('/orders')
def orders():
    orders = order_repository.select_all()
    return render_template("/orders/index.html", orders = orders)
