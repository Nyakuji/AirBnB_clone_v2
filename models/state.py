#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Init inherited"""
        super().__init__(*args, **kwargs)
    
    if models.storage_type != "db":
        @property
        def cities(self):
            """
            getter attribute cities that returns the list of City instances with state_id equals to the current State.id =>
            It will be the FileStorage relationship between State and City
            """
            list_city =[]
            all_inst_c = models.storage.all(City)
            for value in all_inst_c.values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city