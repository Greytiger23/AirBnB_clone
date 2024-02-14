#!/usr/bin/python3
import uuid
from datetime import datetime
"""module that defines the base class"""


class BaseModel:
    """represents the class"""
    def __init__(self, *args, **kwargs):
        """public instance method"""
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """public method"""
        return "[{}] ({]) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """public instance method"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """punlic instance method"""
        obj_dict = {}
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()
            else:
                obj_dict[key] = value
        return obj_dict
