#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import getenv


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
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
    else:
        d = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
