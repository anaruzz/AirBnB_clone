#!/usr/bin/python3


""" Amenity test suite"""

from models.base_model import BaseModel
from models.place import Amenity
import unittest



class TestAmenity(unittest.TestCase):
    """ Amenity unit tests"""


    def test_Amenity_object_should_be_of_type_Amenity(self):
        """
        test if the object is an amenity instance
        """
        model = Amenity()
        self.assertEqual(type(model), Amenity)

    def test_name_is_string(self):
        model = Amenity()
        self.assertEqual(type(model.name), str)
