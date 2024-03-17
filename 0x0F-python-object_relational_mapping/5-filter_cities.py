#!/usr/bin/python3
"""Lists all cities of state from database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv, exit

if __name__ == '__main__':

    if len(argv) != 5:
        print("Usage: {} username password database state_name"
              .format(argv[0]))
        exit(1)

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
        cursor = db.cursor()
        query = """
                SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC
                """
        cursor.execute(query, (argv[4],))

        row = cursor.fetchone()
        if row[0]:
            print(row[0])
        else:
            print("No cities found for the given state.")

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        exit(1)
