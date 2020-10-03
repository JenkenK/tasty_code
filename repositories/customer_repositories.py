from db.run_sql import run_sql

from models.customer import Customer

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)

def save(customer):
    sql = "INSERT INTO customers (name, address, payment, phone_number, service) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [customer.name, customer.address, customer.payment, customer.phone_number, customer.service]
    results = run_sql(sql, values)
    customer.id = results[0]['id']
    return customer

def select_all():
    customers = []

    sql = "SELECT * FROM cutomers"
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['name'], row['address'], row['payment'], row['phone_number'], row['service'])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        customer = Customer(result['name'], result['address'], result['payment'], result['phone_number'], result['service'])
    return customer 