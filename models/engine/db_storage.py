#!/usr/bin/python3
'''
    Engine for DBStorage
'''
from models.state import Base, State
import models
from models import BaseModel
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sys import argv
from os import getenv


class DBStorage:
    '''
        Database Storage class that connects to DB
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Instantiation of DBStorage
        '''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB'),
                                              pool_pre_ping=True))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
            Query the database and send results to user
        '''
        dicts = {}
        if cls is None:
            for item in models.classes.values():
                try:
                    results = self.__session.query(item).all()
                    for obj in results:
                        key = obj.__class__.__name__ + '.' + obj.id
                        dicts[key] = obj
                except:
                    continue
        else:
            results = self.__session.query(models.classes[cls]).all()
            for obj in results:
                key = obj.__class__.__name__ + '.' + obj.id
                dicts[key] = obj
        return dicts

    def new(self, obj):
        '''
            Create a new object and add it to current session
        '''
        self.__session.add(obj)

    def delete(self, obj=None):
        '''
             Delete an object from current session
        '''
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def save(self):
        '''
            Save session of database
        '''
        self.__session.commit()

    def reload(self):
        '''
            create all tables in db and current session
        '''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        '''
            Calls remove() method on the session attribute self.__session
        '''
        self.__session.remove()
