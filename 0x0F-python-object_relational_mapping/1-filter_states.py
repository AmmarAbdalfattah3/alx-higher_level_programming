#!/usr/bin/python3
"""This module lists all states from the database `hbtn_0e_0_usa`"""


import sys
import MySQLdb

if __name__ == "__main__":

    name = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    connection = MySQLdb.connect(user=name, passwd=password, database=db)
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    connection.close()
