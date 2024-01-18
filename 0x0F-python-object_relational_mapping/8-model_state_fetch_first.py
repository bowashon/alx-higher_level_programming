#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a table
    Base.metadata.create_all(engine)
    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).order_by(State.id).first()
    if state_obj:
        print(f"{state_obj.id}: {state_obj.name}")
    else:
        print("Nothing")

    session.close()
