#!/usr/bin/python3
"""
script that prints all City object in database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
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
        obj = session.query(State, City).join(City).order_by(City.id).all()
    [print(f"{state.name}: ({city.id}) {city.name}") for state, city in obj]
