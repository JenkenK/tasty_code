from db.run_sql import run_sql

from models.order import Order

import repositories.order_repository as order_repository
import repositories.restaurant_repository as restaurant_repository
import repositories.customer_repository as customer_repository
import repositories.dish_repository as dish_repository


def save(order):
    sql = "INSERT INTO orders (order_timestamp, customer_id, restaurant_id, dish_id) VALUES (%s, %s, %s, %s) RETURNING *"
    dish_ids = []
    print(order.dishes)
    for dish in order.dishes:
        dish_ids.append(dish.id)
    values = [order.order_timestamp, order.customer.id, order.restaurant.id, dish_ids]
    results = run_sql(sql, values)
    order.id = results[0]['id']
    return order


def select_all():
    orders=[]

    sql = "SELECT * FROM orders"
    results = run_sql(sql)

    for result in results:
        restaurant = restaurant_repository.select(result['restaurant_id'])
        customer = customer_repository.select(result['customer_id'])
        dish = dish_repository.select(result['dish_id'])
        timestamp = result['order_timestamp']
        order = Order(timestamp, customer, restaurant, dish, result['id'])
        orders.append(order)
    return orders


def select(order_id):
    sql = "SELECT * FROM orders WHERE id = %s"
    values = [order_id]
    result = run_sql(sql, values)[0]
    order = Order(result['order_timestamp'], result['customer_id'], result['restaurant_id'], result['dish_id'], result['id'])
    return order


def delete_all():
    sql = "DELETE FROM orders"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM orders WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(order):
    sql = "UPDATE orders SET (order_timestamp, customer_id, restaurant_id, dish_id) = (%s, %s, %s, %s) WHERE id = (%s)"
    values = [order.order_timestamp, order.customer.id, order.restaurant.id, order.dish.id, order.id]
    run_sql(sql, values)

