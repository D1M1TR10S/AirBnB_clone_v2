#!/usr/bin/python3
'''
    Implementation of the State class
'''
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name = ""
        @property
        def cities(self):
            '''
                Getter attribute that returns a list of cities
                (models.classes["City"])
            '''
            city_list = []
            dicti = models.storage.all(models.classes["City"])
            for key, value in dicti.items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
