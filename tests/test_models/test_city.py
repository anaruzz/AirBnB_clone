#!/usr/bin/python3


""" City test suite"""

from models.base_model import BaseModel
from models.place import City
import unittest



class TestCity(unittest.TestCase):
    """ City unit tests"""


    def test_City_object_should_be_of_type_City(self):
        """
        test if the object is a City instance
        """
        model = City()
        self.assertEqual(type(model), City)

    def test_state_id_is_string(self):
        model = City()
        self.assertEqual(type(model.state_id), str)

    def test_name_is_string(self):
        model = City()
        self.assertEqual(type(model.name), str)
