#!/usr/bin/python3
"""
Module to change the name of a State object from the database hbtn_0e_6_usa.
"""


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that changes the name of a State object from the database
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

    # Changing name of State object with id 2 to "New Mexico".
    state = my_session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    my_session.commit()

    # Closing session.
    my_session.close()
