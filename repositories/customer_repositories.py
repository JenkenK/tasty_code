from db.run_sql import run_sql

from models.customer import Customer

def save(customer):
    sql = "INSERT INTO customers (name, address, payment, phone_number, service) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [customer.name, customer.address, customer.payment, customer.phone_number, customer.service]
    results = run_sql(sql, values)
    customer.id = results[0]['id']
    return customer
    