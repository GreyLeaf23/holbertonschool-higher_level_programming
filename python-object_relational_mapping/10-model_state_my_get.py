#!/usr/bin/python3
"""
Module to print the State object with the name passed as argument from the
database hbtn_0e_6_usa.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """Function that prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa."""

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating instance of Session class.
    my_session = Session()

    # Printing State object with the name passed as argument.
    state = my_session.query(State).filter(State.name == argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print("{}".format(state.id))

    # Closing session.
    my_session.close()
