from db.run_sql import run_sql

from models.order import Order

import repositories.order_repository as order_repository


def save(order):
    sql = "INSERT INTO orders (order_timestamp) VALUES %s RETURNING *"
    values = [order.order_timestamp]
    results = run_sql(sql, values)
    order.id = results[0]['id']
    return order