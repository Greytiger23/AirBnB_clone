#!/usr/bin/python3
from models.base_model import BaseModel
"""module that defines the class"""


class Amenity(BaseModel):
    """represents the class"""
    def __init__(self, *args, **kwargs):
        """public instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "")
