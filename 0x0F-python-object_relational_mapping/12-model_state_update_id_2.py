#!/usr/bin/python3
"""
script that changes the name of a State object from the database
hbtn_0e_usa
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
        state_upd = session.query(State).filter_by(id='2').first()
        if state_upd:
            state_upd.name = "New Mexico"
            session.commit()
