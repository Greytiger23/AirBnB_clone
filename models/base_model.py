#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"""module that defines the base class"""


class BaseModel:
    """represents the class"""
    def __init__(self, *args, **kwargs):
        """public instance method"""
        if kwargs:
            for key, value in kwargs.item():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                        '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """public method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__)

    def save(self):
        """public instance method"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """punlic instance method"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict