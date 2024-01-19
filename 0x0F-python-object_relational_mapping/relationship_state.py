#!/usr/bin/python3
"""
    Class State that inherite from a declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    """
        class State that inherite from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=True)
    cities = relationship('City', backref='state', cascade='all, delete')
