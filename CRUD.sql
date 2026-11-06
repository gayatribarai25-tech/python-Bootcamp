CREATE TABLE menu(
    id INTEGER PRIMARY KEY,
    item VARCHAR(255),
    category VARCHAR(100),
    price INTEGER,
    stock INTEGER
);
INSERT INTO menu (id,item, category, price, stock)
VALUES
(1,'Chai', 'Drink', 10, 40),
(2,'Pasta', 'Snack', 14, 50),
(3,'Samosa', 'Snack', 13, 40),
(100,'Maggie', 'Snack', 18, 60),
(200,'Poha', 'Snack', 19, 30),
(300,'Coffee', 'Drink', 19, 40);


SELECT *from menu;
INSERT INTO menu (id,item, category, price, stock)
VALUES(15,'Paratha','Meal',40,25),
(16,'Thali','Meal',90,4);


SELECT *from menu;
UPDATE menu
SET price = price + 1
WHERE category = 'Snack'

UPDATE menu
SET stock = stock - 5
WHERE item = 'Paratha';

UPDATE menu
SET stock = stock - 4
WHERE item = 'Thali';

DELETE FROM menu
WHERE stock = 0 ;

SELECT item, category, price, stock
FROM menu
ORDER BY category ASC, item ASC;
