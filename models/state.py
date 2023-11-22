#!/usr/bin/python3
"""Defines the State model for HBnB project."""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.city import City

storage_setting = os.getenv("HBNB_TYPE_STORAGE")

class State(BaseModel):
    """Represents a state in the HBnB application."""
    __tablename__ = 'states'
    if storage_setting == "db":
        state_name = Column(String(128), nullable=False)
        related_cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        state_name = ""

        @property
        def cities(self):
            """Returns a list of City instances linked to the State."""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]

