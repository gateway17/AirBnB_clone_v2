#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Get amenities of the property """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
