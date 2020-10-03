from db.run_sql import run_sql

from models.restaurant import Restaurant
from models.cuisine import Cuisine
from models.customer import Customer

import repositories.cuisine_repository as cuisine_repository
import repositories.customer_repository as customer_repository


def save(restaurant):
    sql = "INSERT INTO restaurants ( name, address, phone_number, availability, customer, cuisine ) VALUES ( %s, %s, %s,%s, %s, %s ) RETURNING id"
    values = [restaurant.name, restaurant.address, restaurant.phone_number, restaurant.availability, restaurant.customer.id, restaurant.cuisine.id]
    results = run_sql( sql, values )
    restaurant.id = results[0]['id']
    return restaurant

def select_all():
    restaurants=[]

    sql = "SELECT * FROM restaurants"
    results = run_sql(sql)

    for row in results:
        customer = customer_repository.select(row['custormer'])
        cuisine = cuisine_repository.select(row['cuisine'])
        restaurant = Restaurant(row['name'], row['address'], row['phone_number'], row['availability'], customer, cuisine)
        restaurants.append(restaurant)
