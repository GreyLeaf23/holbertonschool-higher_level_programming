#!/usr/bin/python3
"""
Module to list first State object from database hbtn_0e_6_usa.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """Function that lists first State object from database hbtn_0e_6_usa."""

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating instance of Session class.
    my_session = Session()

    # Printing first State object.
    state = my_session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    # Closing session.
    my_session.close()
