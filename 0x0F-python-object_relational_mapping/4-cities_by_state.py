#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name FROM cities\
             INNER JOIN states ON states.id = cities.state_id ORDER\
             BY cities.id ASC")
    cur.execute(query)
    [print(a) for a in cur.fetchall()]
    cur.close()
    db.close()
