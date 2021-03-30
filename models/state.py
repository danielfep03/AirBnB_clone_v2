#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

    def __init__(self, *argv, **kargs):
        """initialization"""
        super().__init__(*argv, **kargs)
