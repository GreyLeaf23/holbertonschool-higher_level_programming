#!/usr/bin/python3
"""
Module to list all cities from database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """Function that lists all cities from database hbtn_0e_4_usa"""

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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        print(row)

    # Close cursor.
    cur.close()

    # Close connection to database.
    cnx.close()
