#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    l_join = session.query(State, City).join(City).order_by(City.id.asc())

    for state, cities in l_join.all():
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))

    session.close()
