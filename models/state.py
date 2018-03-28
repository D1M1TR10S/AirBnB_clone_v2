#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        '''
            Getter attribute that returns a list of cities
        '''
        city_list = []
        dicti = storage.all(City)
        for key, value in dicti:
            if value.state_id == self.id:
                city_list.append(value)
        return city_list
