CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES (1, 'Asha', 'Pune');
INSERT INTO customers VALUES (2, 'Rohit', 'Delhi');
INSERT INTO customers VALUES (3, 'Priya', 'Chennai');
INSERT INTO customers VALUES (4, 'Kabir', 'Mumbai');
INSERT INTO customers VALUES (5, 'Meera', 'Pune');

SELECT *from customers

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item VARCHAR(50),
    amount INTEGER
);

INSERT INTO orders VALUES (101, 1, 'Headphones', 1500);
INSERT INTO orders VALUES (102, 1, 'Phone Case', 400);
INSERT INTO orders VALUES (103, 2, 'Keyboard', 1200);
INSERT INTO orders VALUES (104, 3, 'Mouse', 600);
INSERT INTO orders VALUES (105, 3, 'Laptop Bag', 1800);
INSERT INTO orders VALUES (106, 3, 'Charger', 700);
INSERT INTO orders VALUES (107, NULL, 'Notebook', 150);
INSERT INTO orders VALUES (108, NULL, 'Pen Drive', 500);


--Report 1
SELECT customers.name, orders.item
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id
WHERE customers.city = 'Pune'
ORDER BY customers.name ASC, orders.item ASC;


--Report 2
SELECT customers.name, customers.city
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
ORDER BY customers.name ASC;

--Report 3
SELECT orders.id, orders.item, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id
WHERE customers.id IS NULL
ORDER BY orders.amount ASC;

--Report 4
SELECT customers.name, orders.item, orders.amount
FROM customers
LEFT JOIN orders
ON customers.id = orders.customer_id
ORDER BY customers.name ASC, orders.amount ASC;

