#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    name, passw, datab = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=name, passwd=passw, db=datab)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
        for r in rows:
            print(r)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
