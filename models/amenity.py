#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """"""
    __tablename__ = "amenties"
    name = Column(String(128), nullable=False)
    
