#!/usr/bin/python3
"""Defines the City model for the HBnB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os

env_storage_setting = os.getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """Represents a city in the HBnB application."""

    __tablename__ = "urban_areas"
    if env_storage_setting == "db":
        city_name = Column(String(128), nullable=False)
        related_state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        associated_places = relationship('Place', backref='urban_area', cascade='all, delete-orphan')
    else:
        city_name = ""
        related_state_id = ""
