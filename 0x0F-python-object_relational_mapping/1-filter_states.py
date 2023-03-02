#!/usr/bin/python3
"""This module  lists all states with a name starting
   with N (upper N) from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if __name__ == "__main__":
    local_host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=local_host, port=port, user=user,
                         passwd=passwd, db=database)
    data_base = db.cursor()
    data_base.execute("SELECT * FROM `states`")
    for state in data_base.fetchall():
        if state[1][0] == "N":
            print(state)
