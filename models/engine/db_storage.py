#!/usr/bin/python3
"""new class for sqlAlchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import json
import sqlalchemy
import models


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host,
                                              db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

        sec = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(sec)

    def all(self, cls=None):
        """returns a dictionary
        Return:
        returns a dictionary of __object
        """
        dic = {}
        if cls:
            query = self.__session.query(cls).all()
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            list_class = [State, City,  User, Place,
                          Review, Amenity, BaseModel]
            for class_s in list_class:
                query = self.__session.query(class_s).all()
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """commit all changes of the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(sec)
        self.__session = session()

    def close(self):
        self.__session.close()
