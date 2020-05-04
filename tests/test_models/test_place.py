#!/usr/bin/python3


""" Place test suite"""

from models.base_model import BaseModel
from models.place import Place
import unittest



class TestPlace(unittest.TestCase):
    """ Place unit tests"""


    def test_Place_object_should_be_of_type_Place(self):
        """
        test if the object is a Place instance
        """
        model = Place()
        self.assertEqual(type(model), Place)

    def test_city_id_is_string(self):
        model = Place()
        self.assertEqual(type(model.city_id), str)

    def test_user_id_is_string(self):
        model = Place()
        self.assertEqual(type(model.user_id), str)
