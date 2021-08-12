#!/usr/bin/python3
""" New engine DBStorage: (models/engine/db_storage.py)"""

from sys import argv
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models.base_model import Base


HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
HBNB_ENV = os.getenv('HBNB_ENV')


class DBStorage():
    """Storage data in Databse """
    __engine = None
    __session = None

    def __init__(self):
        """Initiaze engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
            pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata().drop_all(bind=self.__engine, checkfirst=True)

    def all(self, cls=None):
        """return a dictionary: (like FileStorage)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        if cls is not None:
            my_dict = {}
            for instance in self.__session.query(cls):
                key = str(cls.__name__) + '.' + str(instance.id)
                my_dict[key] = instance
            return(my_dict)
        else:
            my_list = [User, State, City, Amenity, Place, Review]
            for element in my_list:
                for instance in self.__session.query(element):
                    key = instance.__name__ + '.' + str(instance.id)
                    my_dict[key] = instance
            return(my_dict)

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            expire_on_commit=False, bind=self.__engine))
