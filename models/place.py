#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete, delete-orphan', backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                         backref="place_amenities",
                         viewonly=False,
                         primaryjoin="Place.id == place_amenity.c.place_id",
                         secondaryjoin="Amenity.id == place_amenity.c.amenity_id")

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
        @property
        def amenities(self):
            """that returns the list of Amenity"""
            return self.amenity_ids
        
        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute"""
            if type(obj) == "Amenity" and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)


