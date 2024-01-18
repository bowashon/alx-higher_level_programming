#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create table
    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_obj = session.query(State).filter(State.name.like('%a%')).all()
        for state in state_obj:
            session.delete(state)
        session.commit()
