from db.run_sql import run_sql

from models.restaurant import Restaurant
from models.cuisine import Cuisine
from models.customer import Customer

import repositories.cuisine_repository as cuisine_repository
import repositories.customer_repository as customer_repository


def save(restaurant):
    sql = "INSERT INTO restaurants ( name, address, phone_number, availability, cuisine_id ) VALUES ( %s, %s, %s,%s, %s) RETURNING id"
    values = [restaurant.name, restaurant.address, restaurant.phone_number, restaurant.availability, restaurant.cuisine.id]
    results = run_sql(sql, values)
    restaurant.id = results[0]['id']
    return restaurant


def select_all():
    restaurants=[]

    sql = "SELECT * FROM restaurants"
    results = run_sql(sql)

    for row in results:
        cuisine = cuisine_repository.select(row['cuisine_id'])
        restaurant = Restaurant(row['name'], row['address'], row['phone_number'], row['availability'], cuisine, row['id'])
        restaurants.append(restaurant)
    return restaurants


def delete_all():
    sql = "DELETE FROM restaurants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM restaurants WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def cuisine(restaurant):
    sql = "SELECT * FROM cuisine WHERE id = %s"
    values = [restaurant.cuisine.id]
    results = run_sql(sql, values)[0]
    cuisine = Cuisine(results['cuisine'], results['id'])
    return cuisine