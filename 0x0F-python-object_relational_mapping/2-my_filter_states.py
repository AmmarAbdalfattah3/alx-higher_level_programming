#!/usr/bin/python3
"""This module takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument.
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
    data_base.execute("SELECT * FROM states WHERE name='{}' ORDER BY id;"
                      .format(sys.arv[4]))
    for state in data_base.fetchall():
        print(state)
    db.close()
    data_base.close()
