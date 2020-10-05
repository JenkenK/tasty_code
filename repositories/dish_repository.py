from db.run_sql import run_sql

from models.dish import Dish

import repositories.dish_repository as dish_repository
import repositories.restaurant_repository as restaurant_repository


def save(dish):
    sql = "INSERT INTO dishes (name, price, description, restaurant_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [dish.name, dish.price, dish.description, dish.restaurant.id]
    results = run_sql(sql, values)
    dish.id = results[0]['id']
    return dish


def select_all():
    dishes=[]

    sql = "SELECT * FROM dishes"
    results = run_sql(sql)

    for result in results:
        restaurant = restaurant_repository.select(result['restaurant_id'])
        dish = Dish(result['name'], result['price'], result['description'], restaurant, result['id'])
        dishes.append(dish)
    return dishes


def select(dish_id):
    sql = "SELECT * FROM dishes WHERE id = %s"
    values = [dish_id]
    result = run_sql(sql, values)[0]
    dish = Dish(result['name'], result['price'], result['description'], result['restaurant_id'], result['id'])
    return dish


def delete_all():
    sql = "DELETE FROM dishes"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM dishes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(dish):
    sql = "UPDATE dishes SET (name, price, description, restaurant_id) = (%s, %s, %s, %s) WHERE id = (%s)"
    values = [dish.name, dish.price, dish.description, dish.restaurant.id, dish.id]
    run_sql(sql, values)