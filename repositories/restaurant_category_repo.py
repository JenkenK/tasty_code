from db.run_sql import run_sql
from models.restaurant_category import RestaurantCategory

def save(restaurant_category):
    sql = "INSERT INTO restaurant_category (category) VALUES (%s) RETURNING *"
    values = [restaurant_category.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    restaurant_category.id = id

def select_all():
    restaurant_categories = []
    sql = "SELECT * FROM restaurant_category"
    results = run_sql(sql)
    for result in results:
        restaurant_category = RestaurantCategory(result['category'], result['id'])
        restaurant_categories.append(restaurant_category)
    return restaurant_categories

def select(id):
    sql = "SELECT * FROM restaurant_category WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    resturant_category = RestaurantCategory(result['category'], result['id'])
    return resturant_category

def delete_all():
    sql = "DELETE FROM restaurant"
    run_sql(sql)

def update(restaurant_category):
    sql = "UPDATE restaurant_category SET name = %s WHERE id = %s"
    values = [restaurant_category.name, restaurant_category.id]
    run_sql(sql, values)