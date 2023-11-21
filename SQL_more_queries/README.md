# SQL - More Queries Learning!


## General Questions:


### How to create a new MySQL user?
To create a new MySQL user, you can use the CREATE USER statement. Here's an example:

```ruby
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

This statement creates a new user newuser on the localhost host with the password password.

After creating the user, you typically want to grant some privileges to the user. You can do this with the GRANT statement. For example:

```ruby
GRANT ALL PRIVILEGES ON database_name.* TO 'newuser'@'localhost';
```

This statement grants all privileges on the database_name database to newuser.

Finally, you should run the FLUSH PRIVILEGES command to reload the grant tables, making the new privileges take effect:

```ruby
FLUSH PRIVILEGES;
```

Remember, you need to have the necessary privileges to create a user and grant privileges.



### How to manage privileges for a user to a database or table?
In MySQL, you can manage privileges for a user to a database or table using the GRANT and REVOKE statements.


**Granting Privileges**

To grant privileges, you use the GRANT statement. Here's an example:

```ruby
GRANT SELECT, INSERT, DELETE ON database_name.table_name TO 'username'@'localhost';
```

This statement grants SELECT, INSERT, and DELETE privileges on table_name in database_name to username.

If you want to grant all privileges, you can use ALL:

```ruby
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
```

After granting privileges, you should run the FLUSH PRIVILEGES command to make the new privileges take effect:

```ruby
FLUSH PRIVILEGES;
```


**Revoking Privileges**

To revoke privileges, you use the REVOKE statement. Here's an example:

```ruby
REVOKE SELECT, INSERT, DELETE ON database_name.table_name FROM 'username'@'localhost';
```

This statement revokes SELECT, INSERT, and DELETE privileges on table_name in database_name from username.

After revoking privileges, you should also run the FLUSH PRIVILEGES command:

```ruby
FLUSH PRIVILEGES;
```

Remember, you need to have the necessary privileges to grant or revoke privileges.



### What’s a PRIMARY KEY?
A PRIMARY KEY is a column (or a set of columns) in a table that uniquely identifies each row in that table.

The PRIMARY KEY constraint has the following characteristics:

It must contain unique values. If the primary key consists of multiple columns, the combination of values in these columns must be unique.
It must contain a value (i.e., it cannot contain NULL).
A table can have only one primary key.
Here's an example of how to set a primary key in a table:

```ruby
CREATE TABLE Employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(255)
);
```

In this example, ID is the primary key for the Employees table. Each ID value must be unique and cannot be NULL.



### What’s a FOREIGN KEY?
A FOREIGN KEY is a column (or a set of columns) in a table that is used to establish a link between the data in two tables. The FOREIGN KEY in one table points to a PRIMARY KEY in another table.

The table containing the FOREIGN KEY is called the child table, and the table containing the candidate key is called the referenced or parent table.

Here's an example of how to set a foreign key in a table:

```ruby
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderNumber INT,
    EmployeeID INT,
    FOREIGN KEY (EmployeeID) REFERENCES Employees(ID)
);
```

In this example, EmployeeID in the Orders table is a foreign key that references ID in the Employees table. This means that for each order, the EmployeeID
must be a valid ID in the Employees table.



### How to use NOT NULL and UNIQUE constraints?
In SQL, the NOT NULL and UNIQUE constraints are used to enforce certain rules on the data in a table.

**NOT NULL**

The NOT NULL constraint ensures that a column cannot have a NULL value. Here's an example:

```ruby
CREATE TABLE Employees (
    ID INT NOT NULL,
    Name VARCHAR(255) NOT NULL
);
```

In this example, both the ID and Name columns cannot have NULL values.

**UNIQUE**

The UNIQUE constraint ensures that all values in a column are different. Here's an example:

```ruby
CREATE TABLE Employees (
    ID INT NOT NULL UNIQUE,
    Name VARCHAR(255) NOT NULL
);
```

In this example, all ID values must be unique, i.e., no two rows can have the same ID.

You can also use these constraints when altering a table. For example:

```ruby
ALTER TABLE Employees
ADD Email VARCHAR(255) NOT NULL UNIQUE;
```

This adds a new Email column to the Employees table, and ensures that it cannot have NULL values and that all values must be unique.



### How to retrieve datas from multiple tables in one request?
To retrieve data from multiple tables in one request, you can use the JOIN clause in SQL. The JOIN clause combines rows from two or more tables based on a related column between them.

Here's an example:

```ruby
SELECT Orders.OrderID, Employees.Name
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.ID;
```

This SQL statement selects OrderID from the Orders table, and Name from the Employees table, where the EmployeeID in the Orders table matches the ID in the
Employees table.

There are different types of SQL joins: INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN. The type of join you use determines which records are included in
the result set.



### What are JOIN and UNION?
JOIN and UNION are two operations in SQL that allow you to retrieve data from multiple tables.


**JOIN**

A JOIN clause is used to combine rows from two or more tables, based on a related column between them. There are several types of JOIN operations, including
INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN.

Here's an example of a JOIN:

```ruby
SELECT Orders.OrderID, Employees.Name
FROM Orders
INNER JOIN Employees ON Orders.EmployeeID = Employees.ID;
```

This statement returns the OrderID from the Orders table and the Name from the Employees table, where the EmployeeID in the Orders table matches the ID in
the Employees table.


**UNION**

The UNION operator is used to combine the result set of two or more SELECT statements. Each SELECT statement within the UNION must have the same number of
columns, and the columns must be of compatible data types.

Here's an example of a UNION:

```ruby
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

This statement returns the combined result set of the two SELECT statements. Note that UNION automatically removes duplicate rows. If you want to keep
duplicate rows, you can use UNION ALL instead.
