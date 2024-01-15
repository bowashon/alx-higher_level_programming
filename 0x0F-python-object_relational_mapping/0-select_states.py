#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_use
connect to database through mysql username, mysql password, and database name
Usage: ./0-select_states.sql <mysql username>, <mysql password> <database>
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    my_cursor = db.cursor()
    my_cursor.execute("SELECT * FROM states")
    [print(state) for state in my_cursor.fetchall()]
    my_cursor.close()
    db.close()
