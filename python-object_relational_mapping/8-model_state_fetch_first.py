#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    state_first_obj = session.query(State).order_by(State.id).first()
    if state_first_obj:
        print("{}: {}".format(state_first_obj.id, state_first_obj.name))
    else:
        print('Nothing')

    session.close()
