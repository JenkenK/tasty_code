DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS cuisines;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    payment VARCHAR(255),
    phone_number BIGINT, ---can use varchar(15) and strip out all non-numeric data
    service VARCHAR(255)
);

CREATE TABLE food (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    description VARCHAR(255)  
);

CREATE TABLE cuisines (
    id SERIAL PRIMARY KEY, 
    cuisine VARCHAR(255)
);


CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT, 
    phone_number BIGINT, 
    availability BOOLEAN,
    cuisines_id INT REFERENCES cuisines(id)
    -- food_id SERIAL REFERENCES food(id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY, -- this is my order number
    -- order_number INT,
    order_timestamp TIMESTAMP, ---DEFAULT NOW, try include time of order from now
    customer_id SERIAL REFERENCES customers(id) ON DELETE CASCADE, 
    restaurant_id SERIAL REFERENCES restaurants(id) ON DELETE CASCADE
    --   review TEXT
);
