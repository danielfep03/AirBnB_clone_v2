#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'Amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("place", secondary='place_amenity')
    else:
        name = ""
