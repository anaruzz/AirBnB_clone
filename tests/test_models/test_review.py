#!/usr/bin/python3


""" Review test suite"""

from models.base_model import BaseModel
from models.review import Review
import unittest



class TestReview(unittest.TestCase):
    """ Review unit tests"""


    def test_Review_object_should_be_of_type_Review(self):
        """
        test if the object is a Review instance
        """
        model = Review()
        self.assertEqual(type(model), Review)

    def test_place_id_is_string(self):
        model = Review()
        self.assertEqual(type(model.place_id), str)

    def test_user_id_is_string(self):
        model = Review()
        self.assertEqual(type(model.user_id), str)
