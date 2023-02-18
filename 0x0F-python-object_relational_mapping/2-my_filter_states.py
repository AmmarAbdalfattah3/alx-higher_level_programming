#!/usr/bin/python3
"""This module takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument.
"""


import sys
import MySQLdb

if __name__ == "__main__":
    local_host = "localhost"
    port = 3306
    db = MySQLdb.connect(host=local_host, port=port, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    data_base = db.cursor()
    name = sys.argv[4]
    cmd = "SELECT * FROM states WHERE name='{}' ORDER BY id;".format(name)
    data_base.execute(cmd)
    for state in data_base.fetchall():
        print(state)
    data_base.close()
    db.close()
