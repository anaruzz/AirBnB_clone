#!/usr/bin/python3

"""
Module that converts dictionary representation to a json string
and stores it in a file and vice versa
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import os

class FileStorage:
    """
    Class that serializes instances to a JSON
    file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in the object a key and a value
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serialises __objects to the JSON file
        """
        new_dict = {}
        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as file:
            json_text = json.dumps(new_dict)
            file.write(json_text)

    def reload(self):
        """
        deserialises __objects the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                for k, v in data.items():
                    obj = eval(k.split('.')[0])(**v)
                    self.new(obj)
        except FileNotFoundError:
            pass
