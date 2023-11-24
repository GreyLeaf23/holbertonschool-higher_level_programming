#!/usr/bin/python3
"""
Module to list all State objects that contain the letter 'a' from database
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that lists all State objects that contain the letter 'a' from
    database hbtn_0e_6_usa."""

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating instance of Session class.
    my_session = Session()

    # Printing State objects.
    for state in my_session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))

    # Closing session.
    my_session.close()
