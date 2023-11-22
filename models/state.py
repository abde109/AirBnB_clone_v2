#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class for HBNB project, represents a state in the database. """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # If using db storage, define a relationship to the City class
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        # If using file storage, create a property to return list of cities
        @property
        def cities(self):
            """Get a list of cities with the state's id."""
            from models import storage
            all_cities = storage.all(City)
            state_cities = [city for city in all_cities.values() if city.state_id == self.id]
            return state_cities



