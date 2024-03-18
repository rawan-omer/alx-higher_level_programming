#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
