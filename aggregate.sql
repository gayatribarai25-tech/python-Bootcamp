-- Query 1 - Each city with its total amount (total), biggest first (INNER JOIN)

SELECT customers.city,SUM(orders.amount) AS total
FROM customers 
INNER JOIN orders
ON customers.id = orders.customer_id 
GROUP BY customers.city
ORDER BY total DESC
SELECT * FROM orders



-- Query 2 - Each item with its number of orders (num_orders) and total, most orders first, then by item

SELECT orders.item, COUNT(orders.item) AS num_orders
FROM orders
INNER JOIN customers
ON customers.id = orders.customer_id
GROUP BY orders.item
ORDER BY num_orders DESC, orders.item ASC;