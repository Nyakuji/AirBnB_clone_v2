#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Init inherited"""
        super().__init__(*args, **kwargs)
    
    #For DBStorage
    if models.storage_type == "db":
        cities = relationship('City', backref='state',
                              cascade='all,delete-orphan')
        
    #For FileStorage
    else:
        @property
        def cities(self):
            """Getter attribute for cities in FileStorage"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        
