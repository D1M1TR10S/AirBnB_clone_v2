#!/usr/bin/python3
'''
    Define the class City.
'''
from models.base_model import BaseModel


class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    state_id = Column(String(60), foreign_key("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
