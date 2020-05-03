#!usr/bin/python3


""" BaseModel test suite"""

from models.basemodel import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """ BaseModel unit tests"""

    model = BaseModel()

    def test_base_object_should_be_of_type_BaseModel(self):
        """
        test if the object is a BaseModel instance
        """
        self.assertEqual(type(model), BaseModel)

    def test_to_dict_method(self):
        """
        test if updated_at, created_at, id, class name
        are all in the to_dict method
        """
        self.assertEqual('updated_at' in model.to_dict())
        self.assertEqual('created_at' in model.to_dict())
        self.assertEqual('id' in model.to_dict())
        self.assertEqual('__class__' in model.to_dict())

    def test_base_object_has_id(self):
        """
        test if a basemodel object has an id
        """
        self.assertIsNotNone(model.id)

    def test_created_at_attribute:
        """
        test if the created_at attribute is of type datetime
        """
        self.assertIs(self.created_at, datetime.datetime)

    def test_save_updated_at_attribute(self):
        """
        test if the method save changes the updated_at attribute
        to current time
        """
        last_update = model.updated_at
        model.save()
        self.assertEqual(last_update, model.updated_at)

    def test_str_method(self):
        """
        test if the class name is in the str representation
        """
        model_string = str(model)
        self.assertEqual("[BaseModel]" in model_string, True)
