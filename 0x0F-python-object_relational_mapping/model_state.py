#!/usr/bin/python3
"""
Using SQLAlchemy
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Defines a class State that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
