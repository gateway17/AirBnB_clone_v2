#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    name = ""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        cities_isinstance = []
        obj_dict = storage.all(City)
        for key, value in obj_dict.items():
            if self.id == value.state_id:
                cities_isinstance.append(value)
        return(cities_isinstance)
