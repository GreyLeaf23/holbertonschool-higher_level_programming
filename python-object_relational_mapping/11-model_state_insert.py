#!/usr/bin/python3
"""
Module to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that adds the State object "Louisiana" to the database
    hbtn_0e_6_usa."""

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating instance of Session class.
    my_session = Session()

    # Creating new State object.
    new_state = State(name="Louisiana")

    # Adding new State object to current database session.
    my_session.add(new_state)

    # Committing all changes.
    my_session.commit()

    # Printing new State object's id.
    print("{}".format(new_state.id))

    # Closing session.
    my_session.close()
