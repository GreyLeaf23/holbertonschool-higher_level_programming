#!/usr/bin/python3
"""
Module to take user input and display all values in the states table of
hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Function that takes user input and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    """

    # Connecting to a MySQL database.
    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # Making cursor obj for execution.
    cur = cnx.cursor()

    # Executing query.
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC",
        (sys.argv[4],))

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        if row[1][0] == sys.argv[4][0]:
            print(row)

    # Close cursor.
    cur.close()

    # Close connection to database.
    cnx.close()
