#!/usr/bin/python3
"""This script adds the State object “Louisiana”
   to the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    new_state = State(name="Louisiana")

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(new_state)
    session.commit()

    print(new_state.id)
