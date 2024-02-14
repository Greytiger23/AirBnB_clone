#!/usr/bin/python3
"""module that defines the FileStorage class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """represents the class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public instance method"""
        return FileStorage.__objects

    def new(self, obj):
        """public instance method"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """public instance method"""
        a = {}
        for key, obj in FileStorage.__objects.items():
            a[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(a, file)

    def reload(self):
        """public instance method"""
        try:
            with open(FileStorage.__file_path) as file:
                a = json.load(file)
                for value in a.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    n = eval(class_name)
                    self.new(n(**value))
        except FileNotFoundError:
            pass
