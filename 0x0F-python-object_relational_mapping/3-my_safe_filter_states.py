#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the state
table of hbtn_0e_0_usa where name matches the argument. But this
time, write one that is safe from MySQL injection
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '%s'"
    cur.execute(query, sys.argv[4])
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
