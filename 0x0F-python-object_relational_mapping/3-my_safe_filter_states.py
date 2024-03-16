#!/usr/bin/python3
"""This module takes in arguments and displays all values in
   the states table of hbtn_0e_0_usa where name matches
   the argument. But this time, write one that
   is safe from MySQL injections!
"""


import sys
import MySQLdb

if __name__ == "__main__":

    name = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    name_input = sys.argv[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=name,
        passwd=password,
        database=db)
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name='{:s}'\
            ORDER BY states.id ASC;".format(name_input))

    for row in cur.fetchall():
        print(row)

    cur.close()
    connection.close()
