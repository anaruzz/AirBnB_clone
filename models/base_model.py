#!/usr/bin/python3

"""
Module that defines the class BaseModel
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    Class that defines common attributes and methods for
    the other classes
    """
    def __init__(self, *args, **kwargs):
        """
        BaseModel instance constructor
        """
        if args:
            pass
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        a = '%Y-%m-%dT%H:%M:%S.%f'
                        setattr(self, key, datetime.strptime(value, a))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        ncl = self.__class__.__name__
        string = "[{}] ({}) {}".format(ncl, self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        dic['__class__'] = self.__class__.__name__
        return dic
