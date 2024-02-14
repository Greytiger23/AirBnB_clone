#!/usr/bin/python3
import json
from json import dump
from json import load
from models.base_model import BaseModel
"""module that defines the FileStorage class"""


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
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            dump(a, file)

    def reload(self):
        """public instance method"""
        c = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as file:
                s = load(file)
                for value in s.values():
                    class_name = value["__class__"]
                    class_obj = c[class_name]
                    self.new(class_obj(**value))
        except FileNotFoundError:
            pass
