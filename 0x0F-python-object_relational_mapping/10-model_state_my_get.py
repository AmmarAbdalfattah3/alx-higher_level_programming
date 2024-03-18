#!/usr/bin/python3
"""This module prints the State object with the name
   passed as argument from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(State.name == name).first()

    if row:
        print(row.id)
    else:
        print("Not found")
    session.close()
