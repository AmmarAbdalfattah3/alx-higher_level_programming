#!/usr/bin/python3
"""This script prints the first State object
   from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()

    if row is None:
        print("Nothing")
    else:
        print("{}: {}".format(row.id, row.name))
    session.close()
