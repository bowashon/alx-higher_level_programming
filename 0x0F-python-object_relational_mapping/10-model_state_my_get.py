#!/usr/bin/python3
"""
script that print the State object with the name passed as an
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state_obj = session.query(State).filter(State.name == argv[4]).first()
    if state_obj:
        print(state_obj.id)
    else:
        print("Not found")
