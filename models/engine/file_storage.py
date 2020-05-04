#!/usr/bin/python3

"""
Module that converts dictionary representation to a json string
and stores it in a file and vice versa
"""
import json
from models.base_model import BaseModel
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
            if type(val) is dict:
                new_dict[key] = val
            else:
                new_dict[key] = val.to_dict()
        with open(self.__file_path, mode="w") as file:
            json_text = json.dumps(new_dict)
            file.write(json_text)

    def reload(self):
        """
        deserialises __objects the JSON file to __objects
        """
        if os.stat(self.__file_path):
            if os.stat(self.__file_path).st_size != 0:
                with open(self.__file_path, 'r') as file:
                    data = json.load(file)
                    for k, v in data.items():
                        obj = eval(k.split('.')[0])(**v)
                        self.new(obj)
