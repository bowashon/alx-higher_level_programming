#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a from
the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create table
    Base.metadata.create_all(engine)
    # create a Session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_obj = session.query(State).filter(State.name.like('%a%'))\
                                        .order_by(State.id).all()
    [print("{}: {}".format(state.id, state.name)) for state in state_obj]
