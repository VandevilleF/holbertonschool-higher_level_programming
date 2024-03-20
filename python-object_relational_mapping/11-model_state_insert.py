#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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

    # Creat new instance
    state_obj = State(name="Louisiana")
    # Add to database
    session.add(state_obj)
    # commits the current transaction for the specified db connection
    session.commit()

    print("{}".format(state_obj.id))
    session.close()
