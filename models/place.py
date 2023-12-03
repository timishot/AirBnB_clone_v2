#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete, delete-orphan', backref="place")
    else:
        @property
        def reviews(self):
            """returns the list of Review instances"""
            var = models.FileStorage.all()
            lis = []
            result = []
            for key in var:
                review = key.replace(".", " ")
                review = review.split()
                if review[0] == "review":
                    lis.append(var[key])
            for elem in lis:
                if (elem.place_id == self.id):
                    result.append(elem)
            return result
