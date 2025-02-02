#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from os import getenv


class Amenity(BaseModel, Base):
    """Creates an Amenity class"""
    __tablename__ = 'amenities'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)

        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60),
                                     ForeignKey('places.id'),
                                     primary_key=True, nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True, nullable=False))
    else:
        name = ""
