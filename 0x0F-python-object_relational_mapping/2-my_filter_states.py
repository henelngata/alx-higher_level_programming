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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
