# SQL - Introduction Learning!

## General Questions:



### What's a database?
A database is an organized collection of data stored and accessed electronically. It is designed to hold data that is structured in a way that makes it
easily accessible, manageable, and updateable. Databases can handle data that includes everything from small amounts to large volumes of data across
multiple servers.


### What's a relational database?
A relational database is a type of database that organizes data into tables, and these tables can be linked—or related—based on data common to each. This
type of database is based on the relational model, introduced by E.F. Codd. In a relational database, each row in the table is a record with a unique ID
called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish
the relationships among data points.


### What does SQL stands for?
SQL stands for Structured Query Language. It's a programming language used to communicate with and manipulate databases. Most of the relational database
management systems (RDBMS) like MySQL, MS Access, Oracle, Sybase, Informix, and PostgreSQL use SQL as their standard database language.


### What's MySQL?
MySQL is an open-source relational database management system (RDBMS) that uses SQL (Structured Query Language) for adding, removing, and modifying
information in the database. Standard SQL commands, such as ADD, DROP, INSERT, and UPDATE can be used with MySQL. It's known for its quick processing,
proven reliability, ease and flexibility of use. MySQL is an essential part of almost every open source PHP application. Good examples for PHP & MySQL-based
scripts are WordPress, Joomla, Magento and Drupal.


### How to create a database in MySQL?
To create a database in MySQL, you can use the CREATE DATABASE SQL statement. Here's an example:

```ruby
CREATE DATABASE database_name;
```

Replace database_name with the name you want to give to your database.

Remember, you need to have the necessary privileges to create a database. Also, the database name must be unique within an instance of MySQL server.

After creating the database, you can use it by executing the following command:

```ruby
USE database_name;
```

This sets the newly created database as the current database for your MySQL connection session.


### What does DDL and DML stand for?
DDL stands for Data Definition Language. It is used in SQL to define and manage the structure of the database. DDL commands include CREATE, ALTER, and DROP.

DML stands for Data Manipulation Language. It is used in SQL to retrieve, insert, delete, and modify the data in the database. DML commands include SELECT,
INSERT, UPDATE, and DELETE.


### How to CREATE or ALTER a table?
In SQL, you can use the CREATE TABLE statement to create a new table, and the ALTER TABLE statement to modify an existing table.

Here's an example of creating a table:

```ruby
CREATE TABLE Employees (
    ID INT,
    Name VARCHAR(255),
    Salary FLOAT,
    PRIMARY KEY (ID)
);
```

This creates a table named Employees with three columns: ID, Name, and Salary. The ID column is defined as the primary key.

To alter a table, you can use the ALTER TABLE statement. Here's an example:

```ruby
ALTER TABLE Employees
ADD Email VARCHAR(255);
```

This adds a new column named Email to the Employees table.

Remember, you need to have the necessary privileges to create or alter a table in a database.


### How to SELECT data from a table?
To select data from a table in SQL, you use the SELECT statement. Here's an example:

```ruby
SELECT * FROM Employees;
```

This statement selects all data from the Employees table. The * means "all columns".

If you want to select only certain columns, you can specify them instead of *. For example:

```ruby
SELECT Name, Email FROM Employees;
```

This statement selects only the Name and Email columns from the Employees table.

You can also use a WHERE clause to filter rows. For example:

```ruby
SELECT * FROM EThis query returns the current date and time.mployees WHERE Salary > 50000;
```

This statement selects all data from the Employees table where the Salary is greater than 50000.


### How to INSERT, UPDATE or DELETE data?
To insert, update, or delete data in SQL, you use the INSERT, UPDATE, and DELETE statements respectively.

Here's an example of each:

**INSERT**
```ruby
INSERT INTO Employees (ID, Name, Email, Salary)
VALUES (1, 'John Doe', 'john.doe@example.com', 55000);
```

This statement inserts a new row into the Employees table.

**UPDATE**
```ruby
UPDATE Employees
SET Email = 'j.doe@example.com'
WHERE ID = 1;
```

This statement updates the Email of the employee with ID 1.

**DELETE**
```ruby
DELETE FROM Employees WHERE ID = 1;
```

This statement deletes the employee with ID 1 from the Employees table.

Remember, you need to have the necessary privileges to insert, update, or delete data in a database. Also, be careful with the DELETE statement: if you omit
the WHERE clause, it will delete all rows.


### What are subqueries?
A subquery, also known as a nested query or inner query, is a query embedded within another SQL query. It's used to further manipulate the data fetched by
the main query, allowing more complex operations.

Subqueries can be used in various parts of a query, including the SELECT, FROM, WHERE, and HAVING clauses. They can return a single value, a row, a column,
or a table, depending on how they're used.

Here's an example of a subquery in a WHERE clause:

```ruby
SELECT * FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

This query selects all employees whose salary is greater than the average salary of all employees. The subquery (SELECT AVG(Salary) FROM Employees)
calculates the average salary.


### How to use MySQL functions?
MySQL provides various functions that you can use to perform calculations, manipulate strings, work with dates and times, and more.

Here's an example of using some common MySQL functions:

**COUNT()**
```ruby
SELECT COUNT(*) FROM Employees;
```

This query returns the number of rows in the Employees table.

**AVG()**
```ruby
SELECT AVG(Salary) FROM Employees;
```

This query returns the average salary of all employees.

**CONCAT()**
```ruby
SELECT CONCAT(FirstName, ' ', LastName) AS FullName FROM Employees;
```

This query concatenates the FirstName and LastName columns to create a FullName.

**NOW()**
```ruby
SELECT NOW();
```

This query returns the current date and time.
