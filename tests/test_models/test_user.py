#!/usr/bin/python3


""" User test suite"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """ User unit tests"""
    def test_email_is_string(self):
        s = User()
        self.assertEqual(type(s.email), str)

    def test_first_name_is_string(self):
        s = User()
        self.assertEqual(type(s.first_name), str)

    def test_last_name_is_string(self):
        s = User()
        self.assertEqual(type(s.last_name), str)

    def test_user_has_password(self):
        self.assertTrue('password' in User.__dict__)
