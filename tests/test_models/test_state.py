#!/usr/bin/python3


""" State test suite"""

from models.base_model import BaseModel
from models.state import State
import unittest



class TestState(unittest.TestCase):
    """ State unit tests"""


    def test_state_object_should_be_of_type_State(self):
        """
        test if the object is a State instance
        """
        model = State()
        self.assertEqual(type(model), State)

    def test_name_is_string(self):
        model = State()
        self.assertEqual(type(model.name), str)
