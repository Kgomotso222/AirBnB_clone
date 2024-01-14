#!/usr/bin/python3
"""Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class
    Attributes:
        city_id : City id
        user_id : User id
        name : name of the place
        description : description of the place
        number_rooms : number of rooms of the place
        number_bathrooms : number of bathrooms of the place
        max_guest : maximum number of guests of the place
        price_by_night : price by night of the place
        latitude : latitude of the place
        longitude : longitude of the place
        amenity_ids : amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
