#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="delete")
