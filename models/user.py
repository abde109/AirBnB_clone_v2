#!/usr/bin/python3
"""Defines the User model for the HBnB project."""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os

storage_option = os.getenv("HBNB_TYPE_STORAGE")

class User(BaseModel):
    """Representation of a user in the HBnB system."""
    __tablename__ = 'users'
    if storage_option == 'db':
        email = Column(String(128), nullable=False)
        pwd = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places_ref = relationship('Place', backref='user', cascade='all, delete')
        review_ref = relationship('Review', backref='user', cascade='all, delete')
    else:
        email = ""
        pwd = ""
        first_name = ""
        last_name = ""
