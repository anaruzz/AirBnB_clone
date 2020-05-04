#!/usr/bin/python3
"""test for file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    def test_file_path(self):
        """Test the type of file_path"""
        self.assertTrue(isinstance(self.file_path, str))

    def test_objects(self):
        """Test the type of objects"""
        self.assertTrue(isinstance(self.objects, dict))

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        storage.new(user)
        key = self.__class__.__name__ + "." + str(self.id)
        self.assertIsNotNone(obj[key])

    def test_reload(self):
        """Test reload"""
        self.assertTrue(isinstance(self.objects, dict))
