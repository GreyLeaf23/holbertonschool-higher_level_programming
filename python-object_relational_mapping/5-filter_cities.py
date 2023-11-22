#!/usr/bin/python3
"""
Module to take in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Function that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
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
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    print(", ".join([row[0] for row in query_rows]))

    # Close cursor.
    cur.close()

    # Close connection to database.
    cnx.close()
