#!/usr/bin/pytgon3
from models.base_model import BaseModel
"""module that defines the class"""


class User(BaseModel):
    """represents the class"""
    def __init__(self, *args, **kwargs):
        """public instance"""
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")
