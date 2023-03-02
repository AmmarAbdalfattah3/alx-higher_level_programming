#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    data_base = db.cursor()
    data_base.execute("SELECT * FROM `states`")
    for state in data_base.fetchall():
        print(state)
