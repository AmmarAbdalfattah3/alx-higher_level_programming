#!/usr/bin/python3
"""This module lists all cities from
   the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    name = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=name,
        passwd=password,
        database=db)
    cur = connection.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities, states\
            WHERE cities.state_id=states.id ORDER BY cities.id")

    for row in cur.fetchall():
        print(row)

    cur.close()
    connection.close()
