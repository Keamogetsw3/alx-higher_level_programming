#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
