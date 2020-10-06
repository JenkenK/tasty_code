from db.run_sql import run_sql

from models.order_dish import OrderDish

import repositories.order_dish_repository as order_dish_repository
import repositories.dish_repository as dish_repository


def save(order_dish):
    sql = "INSERT INTO order_dishes (order_id, dish_id) VALUES (%s, %s) RETURNING *"
    values = [order_dish.order.id, order_dish.dish.id]
    results = run_sql(sql, values)
    order_dish.id = results[0]['id']
    return order_dish