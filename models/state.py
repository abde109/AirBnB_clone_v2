#!/usr/bin/python3
""" State Module for HBNB project """
import datetime
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref="state")

    def __init__(self, *args, **kwargs):
        """ Initializes State """
        super().__init__(*args, **kwargs)
