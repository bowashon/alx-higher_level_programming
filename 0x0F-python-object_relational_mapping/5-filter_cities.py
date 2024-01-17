#!/usr/bin/python3
"""
this script takes in the name of a state as an argument and lists all
cities of the state, using the database hbtn_0e_4_usa
usage: ./5-filter_cities.py <user> <password> <database> <state>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (sys.argv[4],))
    my_list = [city[0] for city in cur.fetchall()]

    print(", ".join(my_list))
    cur.close()
    db.close()
