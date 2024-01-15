#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
Usage: ./filter_states.py <user name> <password> <database>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
