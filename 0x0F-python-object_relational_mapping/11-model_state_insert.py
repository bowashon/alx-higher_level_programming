#!/usr/bin/python3
"""
script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
using the API mysqlalchemy.orm
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    # create connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create table
    Base.metadata.create_all(engine)
    # create session
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
