#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel and Base
    '''
    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
