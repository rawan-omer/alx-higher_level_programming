#!/usr/bin/python3
"""Displays values in states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()
        for r in rows:
            print(r)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
