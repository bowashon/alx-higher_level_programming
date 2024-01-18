#!/usr/bin/python3
"""
script that lists all State objects from the database hbyn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a table
    Base.metadata.create_all(engine)

    # create a confiqured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    # get all objects of state
    state_obj = session.query(State).order_by(State.id).all()
    # print obj
    for state in state_obj:
        print(f"{state.id}: {state.name}")

    session.close()
