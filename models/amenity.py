#!/usr/bin/python3
'''
    Implementation of the Amenity class
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Amenity(BaseModel, Base):
    '''
        Implementation for the Amenities.
    '''
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        from models.place import association_table
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
            secondary=association_table)

    else:
        name = ""
