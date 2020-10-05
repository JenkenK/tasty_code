from db.run_sql import run_sql

from models.food import Food

import repositories.food_repository as food_repository


def save(food):
    sql = "INSERT INTO foods (name, price, description) VALUES (%s, %s, %s) RETURNING *"
    values = [food.name, food.price, food.description]
    results = run_sql(sql, values)
    food.id = results[0]['id']
    return food


def select_all():
    foods=[]

    sql = "SELECT * FROM foods"
    results = run_sql(sql)

    for result in results:
        food = Food(result['name'], result['price'], result['description'], result['id'])
        foods.append(food)
    return foods


def select(food_id):
    sql = "SELECT * FROM foods WHERE id = %s"
    values = [food_id]
    result = run_sql(sql, values)[0]
    food = Food(result['name'], result['price'], result['description'], result['id'])
    return food


def delete_all():
    sql = "DELETE FROM foods"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM foods WHERE id = %s"
    values = [id]
    run_sql(sql, values)
