DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS restaurant_category;
DROP TABLE IF EXISTS food;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT,
    payment VARCHAR(255),
    phone_number INT,
    service VARCHAR(255)
);

CREATE TABLE food (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price INT,
    description VARCHAR(255)  
);

CREATE TABLE restaurant_category (
    id SERIAL PRIMARY KEY, 
    category VARCHAR(255)
);


CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address TEXT, 
    phone_number INT, 
    availability BOOLEAN,
    restaurant_category_id SERIAL REFERENCES restaurant_category(id),
    food_id SERIAL REFERENCES food(id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY, -- this is my order number
    -- order_number INT,
    order_timestamp TIMESTAMP DEFAULT NOW,
    customer_id SERIAL REFERENCES customers(id) ON DELETE CASCADE, 
    restaurant_id SERIAL REFERENCES restaurants(id) ON DELETE CASCADE
    --   review TEXT
);
