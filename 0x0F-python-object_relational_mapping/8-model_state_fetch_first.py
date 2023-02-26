#!/usr/bin/python3
"""This module lists first State objects from the database hbtn_0e_6_usa"""


import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, str(state)))
    else:
        print("Nothing")
    session.close()
