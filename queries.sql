CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    city VARCHAR(50)
);


INSERT INTO employees (name, department, salary, city)
VALUES
('Rahul', 'HR', 35000, 'Pune'),
('Priya', 'IT', 55000, 'Mumbai'),
('Amit', 'Sales', 42000, 'Delhi'),
('Neha', 'HR', 48000, 'Pune'),
('Rohit', 'IT', 60000, 'Bangalore'),
('Sneha', 'Sales', 52000, 'Mumbai'),
('Karan', 'HR', 39000, 'Delhi'),
('Pooja', 'IT', 45000, 'Pune'),
('Vikas', 'Sales', 47000, 'Bangalore'),
('Meena', 'HR', 51000, 'Mumbai');


SELECT * FROM employees;


-- 1. EMPLOYEES WORKING IN HR

SELECT *
FROM employees
WHERE department = 'HR';

-- Row Count

SELECT COUNT(*)
FROM employees
WHERE department = 'HR';


-- 2. SALARY ABOVE 45000 IN SALES OR IT

SELECT *
FROM employees
WHERE salary > 45000
AND department IN ('Sales', 'IT');

-- Row Count

SELECT COUNT(*)
FROM employees
WHERE salary > 45000
AND department IN ('Sales', 'IT');


-- 3. NAMES CONTAINING LETTER 'e'

SELECT *
FROM employees
WHERE name ILIKE '%e%';

-- Row Count

SELECT COUNT(*)
FROM employees
WHERE name ILIKE '%e%';


-- 4. SALARY BETWEEN 36000 AND 52000
-- SORTED HIGH TO LOW

SELECT *
FROM employees
WHERE salary BETWEEN 36000 AND 52000
ORDER BY salary DESC;

-- Row Count

SELECT COUNT(*)
FROM employees
WHERE salary BETWEEN 36000 AND 52000;


-- 5. FOUR LOWEST SALARIES

SELECT *
FROM employees
ORDER BY salary ASC
LIMIT 4;

-- Row Count

SELECT COUNT(*)
FROM (
    SELECT *
    FROM employees
    ORDER BY salary ASC
    LIMIT 4
) AS lowest_salaries;


-- 6. EMPLOYEES NOT FROM PUNE
-- SORTED BY CITY THEN NAME

SELECT *
FROM employees
WHERE city <> 'Pune'
ORDER BY city ASC, name ASC;

-- Row Count

SELECT COUNT(*)
FROM employees
WHERE city <> 'Pune';


-- 7. TOTAL NUMBER OF EMPLOYEES

SELECT COUNT(*) AS total_employees
FROM employees;