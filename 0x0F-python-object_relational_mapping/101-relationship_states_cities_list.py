#!/usr/bin/python3
"""
List relationship
"""
from relationship_city import City, Base
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create table
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)

    with Session() as session:
        for state in (session.query(State).order_by(State.id).all()):
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")
