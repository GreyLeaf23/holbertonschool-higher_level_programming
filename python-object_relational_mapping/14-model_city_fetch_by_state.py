#!/usr/bin/python3
"""
Module to list all City objects from database hbtn_0e_14_usa.
"""


from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """Function that lists all City objects from database hbtn_0e_14_usa."""

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating instance of Session class.
    my_session = Session()

    # Printing City objects.
    for city, state in my_session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Closing session.
    my_session.close()
