from db.run_sql import run_sql
from models.cuisine import Cuisine

def save(cuisine):
    sql = "INSERT INTO cuisines (cuisine) VALUES (%s) RETURNING *"
    values = [cuisine.cuisine]
    results = run_sql(sql, values)
    id = results[0]['id']
    cuisine.id = id

def select_all():
    cuisines = []
    sql = "SELECT * FROM cuisines"
    results = run_sql(sql)
    for result in results:
        cuisine = Cuisine(result['cuisine'], result['id'])
        cuisines.append(cuisine)
    return cuisines

def select(id):
    sql = "SELECT * FROM cuisines WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    cuisine = Cuisine(result['cuisine'], result['id'])
    return resturant_category

def delete_all():
    sql = "DELETE FROM cuisines"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cuisines WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(cuisine):
    sql = "UPDATE cuisines SET name = %s WHERE id = %s"
    values = [cuisine.name, cuisine.id]
    run_sql(sql, values)