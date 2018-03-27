#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City", backref="state", cascade="delete")
