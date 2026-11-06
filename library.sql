-- 1. Create Database
CREATE DATABASE library_db;

-- 2. Create Books Table
CREATE TABLE books (
    id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100)
);

-- 3. Create Members Table
CREATE TABLE members (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

-- 4. Create Loans Table
CREATE TABLE loans (
    member_id INT,
    book_id INT,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- 5. Insert 4 Books
INSERT INTO books (id, title, author)
VALUES
(1, 'Python Basics', 'John'),
(2, 'JavaScript Guide', 'Smith'),
(3, 'Learn SQL', 'David'),
(4, 'MongoDB Guide', 'Alex');

-- 6. Insert 3 Members
INSERT INTO members (id, name)
VALUES
(1, 'Sama'),
(2, 'Rahul'),
(3, 'Priya');

-- 7. Insert 3 Loans
INSERT INTO loans (member_id, book_id)
VALUES
(1, 2),
(2, 1),
(1, 3);

-- 8. Display All Books
SELECT * FROM books;

-- 9. Display All Members
SELECT * FROM members;

-- 10. Display All Loans
SELECT * FROM loans;


