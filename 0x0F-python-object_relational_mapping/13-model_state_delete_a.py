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

    # Query the database to find all State objects with name containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    if states_to_delete:
        # Delete the State objects
        for state in states_to_delete:
            session.delete(state)
        session.commit()
        print("States deleted successfully")
    else:
        print("No State objects with name containing 'a' found")

    # Close the session
    session.close()
