CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) NOT NULL UNIQUE,
    phone       VARCHAR(20),
    address     VARCHAR(255)
);

CREATE TABLE menu_items (
    item_id     INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price       DECIMAL(10,2) NOT NULL,
    category    VARCHAR(50)
);

CREATE TABLE orders (
    order_id     INT AUTO_INCREMENT PRIMARY KEY,
    customer_id  INT NOT NULL,
    order_date   DATETIME NOT NULL,
    status       VARCHAR(50) NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
    order_id INT NOT NULL,
    item_id  INT NOT NULL,
    quantity INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (order_id, item_id),
    CONSTRAINT fk_od_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
    CONSTRAINT fk_od_item
        FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);

CREATE TABLE payments (
    payment_id   INT AUTO_INCREMENT PRIMARY KEY,
    order_id     INT NOT NULL,
    method       VARCHAR(50) NOT NULL,
    amount       DECIMAL(10,2) NOT NULL,
    payment_date DATETIME NOT NULL,
    status       VARCHAR(50) NOT NULL,
    CONSTRAINT fk_pay_order
        FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email    VARCHAR(150) NOT NULL UNIQUE,
    role     VARCHAR(50) NOT NULL
);

CREATE TABLE restaurant_staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name     VARCHAR(100) NOT NULL,
    role     VARCHAR(50) NOT NULL,
    email    VARCHAR(150) NOT NULL UNIQUE
);