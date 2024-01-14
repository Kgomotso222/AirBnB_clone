#!/usr/bin/python3
"""City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class
    Attributes:
        state_id : state id
        name : name of the city
    """
    state_id = ""
    name = ""
