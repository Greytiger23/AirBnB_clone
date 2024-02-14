#!/usr/bin/python3
from models.base_model import BaseModel
"""module that defines the class"""


class Review(BaseModel):
    """represents the class"""
    def __init__(self, *args, **kwargs):
        """public instance"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get('place_id', "")
        self.user_id = kwargs.get('user_id', "")
        self.text = kwargs.get('text', "")
