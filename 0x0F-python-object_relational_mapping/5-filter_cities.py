#!/usr/bin/python3
"""akes in the name of a state as an argument and lists
  all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":

    name = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=name,
        passwd=password,
        database=db)
    cur = connection.cursor()

    query = "SELECT cities.name FROM cities WHERE cities.state_id=(SELECT id\
            FROM states WHERE name=%s) ORDER BY cities.id ASC"

    cur.execute(query, (state_name,))

    separate = ""
    for row in cur.fetchall():
        print(separate, end="")
        print(row[0], end="")
        separate = ", "
    print()

    cur.close()
    connection.close()
