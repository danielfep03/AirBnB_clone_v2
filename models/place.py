#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


if getenv("HBNB_TYPE_STORAGE") == "db":
    place_amenity = Table('place_amenity', Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", secondary="place_amenity")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        numer_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializate class"""
        super().__init__(*args, **kwargs)

        if getenv('HBNB_TYPE_STORAGE') != "db":
            @property
            def amenities(self):
                """Getter amenities """
                my_list = []
                for x in list(models.storage.all(amenities).value()):
                    if x in self.amenity_ids:
                        my_list.append(x)
                return my_list

            @amenities.setter
            def amenities(self, value):
                """ Set amenities """
                if type(value) == Amenity:
                    self.amenity_ids.append(value.id)
