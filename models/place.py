#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv

association_table = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
)


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
        reviews = relationship("Review", backref="place", cascade="delete")
        amenity_ids = []

        place_amenities = relationship("Amenity",
            secondary=association_table,
            viewonly=False) 
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

        @property
        def reviews(self):
            '''Links Place and Review classes together'''
            obj_dict = models.storage.all(Review)
            review_list = []
            for key, val in obj_dict:
                if val.place_id == self.id:
                    review_list.append(val)
            return review_list

        @property
        def amenities(self):
            '''Returns amenity ids'''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            '''Setter that adds to amenity_ids'''
            if type(obj) == "Amenity":
                dicti = models.storage.all(Amenity)
                for key, amenity in dicti.items():
                    if amenity.id != obj.id:
                        self.amenity_ids.append(obj.id)
