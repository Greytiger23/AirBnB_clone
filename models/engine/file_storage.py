#!/usr/bin/python3
import json
"""module that defines the FileStorage class"""


class FileStorage:
    """represents the class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public instance method"""
        return self.__objects

    def new(self, obj):
        """public instance method"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """public instance method"""
        a = {}
        for key, obj in self.__objects.items():
            a[key] = obj.to_obj()
        with open(self.__file_path, 'w') as file:
            json.dump(a, file)

    def reload(self):
        """public instance method"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    class_name, obj_id = key.split('.')
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
