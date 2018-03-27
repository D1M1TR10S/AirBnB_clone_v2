#!/usr/bin/python3
'''
    Implementation of the State class
'''

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        '''
            Getter attribute that returns a list of cities
        '''
        city_list = []
        dicti = storage.all(City)
        for key, value in dicti:
            if value.state_id == self.id
                city_list.append(value)
        return city_list
