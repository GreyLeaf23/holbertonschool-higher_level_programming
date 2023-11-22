# Python - Object Relational Mapping Learning!

## General Questions:


### How to connect to a MySQL database from a Python script?
To connect to a MySQL database from a Python script, you can use a library like mysql-connector-python. Here's a step-by-step guide:

1. Import the mysql.connector module.
2. Use the connect() function from the mysql.connector module, passing the database details as parameters.
3. Create a cursor object using the cursor() method of the connection object.
4. Use the cursor object to execute SQL queries.

Here's a sample Python script:

```ruby
import mysql.connector

# establish the connection
cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>',
                              database='<database_name>')

# create a cursor object
cursor = cnx.cursor()

# use the cursor object to execute SQL queries
cursor.execute("SELECT * FROM table_name")

# close the connection
cnx.close()
```

GitHub Copilot: To connect to a MySQL database from a Python script, you can use a library like `mysql-connector-python`. Here's a step-by-step guide:

1. Import the `mysql.connector` module.
2. Use the `connect()` function from the `mysql.connector` module, passing the database details as parameters.
3. Create a cursor object using the `cursor()` method of the connection object.
4. Use the cursor object to execute SQL queries.

Here's a sample Python script:

```python
import mysql.connector

# establish the connection
cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>',
                              database='<database_name>')

# create a cursor object
cursor = cnx.cursor()

# use the cursor object to execute SQL queries
cursor.execute("SELECT * FROM table_name")

# close the connection
cnx.close()
```

Remember to replace `<username>`, `<password>`, `<hostname>`, and `<database_name>` with your actual MySQL credentials and database details. Also, replace
`table_name` with the actual table you want to query.



### How to SELECT rows in a MySQL table from a Python script?
To SELECT rows in a MySQL table from a Python script, you can use the execute() method of the cursor object to run a SELECT SQL query. Here's a step-by-step guide:

1. After creating a cursor object, use the execute() method to run a SELECT SQL query.
2. Use the fetchall() method of the cursor object to get all rows from the last executed statement.

Here's a sample Python script:

```ruby
import mysql.connector

# establish the connection
cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>',
                              database='<database_name>')

# create a cursor object
cursor = cnx.cursor()

# use the cursor object to execute a SELECT SQL query
cursor.execute("SELECT * FROM table_name")

# fetch all rows from the last executed statement
rows = cursor.fetchall()

for row in rows:
    print(row)

# close the connection
cnx.close()
```

Remember to replace <username>, <password>, <hostname>, and <database_name> with your actual MySQL credentials and database details. Also, replace
table_name with the actual table you want to query.



### How to INSERT rows in a MySQL table from a Python script?
To INSERT rows in a MySQL table from a Python script, you can use the execute() method of the cursor object to run an INSERT SQL query. Here's a step-by-step guide:

1. After creating a cursor object, use the execute() method to run an INSERT SQL query.
2. Use the commit() method of the connection object to save the changes.

Here's a sample Python script:

```ruby
import mysql.connector

# establish the connection
cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>',
                              database='<database_name>')

# create a cursor object
cursor = cnx.cursor()

# use the cursor object to execute an INSERT SQL query
query = ("INSERT INTO table_name (column1, column2) VALUES (%s, %s)")
data = ('value1', 'value2')
cursor.execute(query, data)

# commit the transaction
cnx.commit()

# close the connection
cnx.close()
```

Remember to replace <username>, <password>, <hostname>, and <database_name> with your actual MySQL credentials and database details. Also, replace
table_name, column1, column2, value1, and value2 with your actual table name, column names, and values.



### What ORM means?
ORM stands for Object-Relational Mapping. It's a programming technique for converting data between incompatible type systems using object-oriented
programming languages. This creates a "virtual object database" that can be used from within the programming language.

In the context of Python, popular ORMs include SQLAlchemy and Django's ORM. They allow you to interact with your database, like you would with SQL. In other
words, they create a Pythonic way to interact with your database.



### How to map a Python Class to a MySQL table?
To map a Python class to a MySQL table, you can use an ORM (Object-Relational Mapping) library like SQLAlchemy. Here's a step-by-step guide:

1. Define a Python class that inherits from sqlalchemy.ext.declarative.declarative_base().
2. In the class, define attributes that match the columns of your MySQL table.
3. Use SQLAlchemy types like String, Integer, etc., to match the data types of your MySQL table columns.

Here's a sample Python script:

```ruby
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# create engine
engine = create_engine('mysql+mysqlconnector://<username>:<password>@<hostname>/<database_name>')

# create tables
Base.metadata.create_all(engine)
```

Remember to replace <username>, <password>, <hostname>, and <database_name> with your actual MySQL credentials and database details. Also, replace the class
attributes and SQLAlchemy types according to your actual table structure.
