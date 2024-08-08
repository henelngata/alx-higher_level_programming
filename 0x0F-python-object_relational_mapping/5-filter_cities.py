#!/usr/bin/python3
"""
using mysqldb to querry a database and return results of a table
"""
import MySQLdb
import sys

if __name__ == '__main__':
    name = sys.argv[1]
    ps = sys.argv[2]
    dbase = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=name, passwd=ps,
                         database=dbase)
    cur = db.cursor()
    query = """SELECT  cities.name FROM cities
                INNER JOIN states ON cities.state_id=states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC"""

    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row), end='')
    cur.close()
    db.close()
