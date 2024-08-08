#!/usr/bin/python3
"""
Contains a script that lists all states with a name starting with N
(upper N) from the database
"""

import MySQLdb
import sys


if __name__ == "__main__":
    name = sys.argv[1]
    ps = sys.argv[2]
    dbase = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=name, passwd=ps,
                         database=dbase)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
