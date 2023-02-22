#!/usr/bin/python3
"""This module lists all cities from the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    local_host = "localhost"
    port = 3306
    db = MySQLdb.connect(host=local_host, port=port, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    data_base = db.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities, states\
           WHERE cities.state_id=states.id ORDER BY cities.id"
    data_base.execute(cmd)
    cities = data_base.fetchall()
    for city in cities:
        print(city)
    data_base.close()
    db.close()
