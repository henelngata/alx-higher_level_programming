#!/usr/bin/python3
"""Contains a model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """A class that represents table states"""
    __tablename__ = 'states'
    id = Column(Integer(11), primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
