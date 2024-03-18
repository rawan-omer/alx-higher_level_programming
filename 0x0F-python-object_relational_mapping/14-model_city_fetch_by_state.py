#!/usr/bin/python3
"""Fetches all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            mysql_username, mysql_password, database_name
        )
    )

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session maker bound to the engine
    DBSession = sessionmaker(bind=engine)

    # Create a session object
    session = DBSession()

    # Query the database to fetch all City objects sorted by id
    cities = session.query(State.name, City).join(City).order_by(City.id).all()

    # Print the results
    for state_name, city in cities:
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()
