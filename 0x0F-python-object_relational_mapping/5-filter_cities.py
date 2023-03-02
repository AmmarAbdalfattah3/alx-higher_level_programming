#!/usr/bin/python3
"""This module  takes in the name of a state as an argument
   and lists all cities of that state, using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    local_host = "localhost"
    port = 3306
    state = sys.argv[4]
    db = MySQLdb.connect(host=local_host, port=port, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    data_base = db.cursor()
    cmd = "SELECT cities.name FROM cities WHERE cities.state_id=(SELECT id\
           FROM states WHERE name='{}') ORDER BY cities.id".format(state,)
    data_base.execute(cmd)
    cities = data_base.fetchall()
    separate = ""
    for city in cities:
        print(separate, end="")
        print(city[0], end="")
        separate = ", "
    print()
    data_base.close()
    db.close()
