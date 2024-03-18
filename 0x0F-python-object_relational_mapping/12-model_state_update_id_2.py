#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
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

    # Query the database to find the State object with id=2
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        # Update the name of the State object
        state_to_update.name = "New Mexico"
        session.commit()
        print("Name updated successfully")
    else:
        print("State with id=2 not found")

    # Close the session
    session.close()
