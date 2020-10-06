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

    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for row in results:
        customer = Customer(row['name'], row['address'], row['payment'], row['phone_number'], row['service'], row['id'])
        customers.append(customer)
    return customers


def select(id):
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    customer = Customer(result["name"], result["address"], result["payment"], result["phone_number"], result["service"], result["id"])
    return customer


def delete(id):
    sql = "DELETE FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(customer):
    sql = "UPDATE customers SET (name, address, payment, phone_number, service) = (%s, %s, %s, %s, %s) WHERE id = (%s)"
    values = [customer.name, customer.address, customer.payment, customer.phone_number, customer.service, customer.id]
    run_sql(sql, values)