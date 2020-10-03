from db.run_sql import run_sql
from models.restaurant_category import RestaurantCategory

def save(restaurant_category):
    sql = "INSERT INTO restaurant_category (category) VALUES (%s) RETURNING *"
    values = [restaurant_category.category]
    results = run_sql(sql, values)
    id = results[0]['id']
    restaurant_category.id = id
    