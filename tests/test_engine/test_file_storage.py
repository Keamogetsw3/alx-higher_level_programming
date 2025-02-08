#!/usr/bin/python3
"""
Unit test suite for the FileStorage engine.
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def test_private_attr(self):
        """
        Test that private attributes of FileStorage are not accessible.
        Ensures that attempts to access __file_path and __objects raise AttributeError.
        """
        base = BaseModel()
        storage = FileStorage()

        # Test instance attributes
        with self.assertRaises(AttributeError):
            file_path = storage.file_path  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            file_path = storage.objects  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            file_path = storage.__objects  # Should not be directly accessible

        # Test class attributes
        with self.assertRaises(AttributeError):
            FileStorage.file_path  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            FileStorage.__file_path  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            FileStorage.objects  # Should not be directly accessible
        with self.assertRaises(AttributeError):
            FileStorage.__objects  # Should not be directly accessible

    def test_reload(self):
        """
        Test the reload() method.
        Ensures that calling reload() does not return any value (should be None).
        """
        storage1 = FileStorage()
        base1 = BaseModel({id: 8})  # Initialize with a dictionary containing an 'id'
        base1.save()
        storage.save()
        self.assertEqual(storage.reload(), None)

    def test_a(self):
        """
        Test that the all() method returns a dictionary.
        """
        storage1 = FileStorage()
        self.assertIsInstance(storage1.all(), dict)

    def test_b(self):
        """
        Test that new() correctly adds an object to storage.
        """
        storage1 = FileStorage()
        base = BaseModel()
        storage1.new(base)  # Add the object to storage
        key = type(base).__name__ + '.' + base.id  # Generate the expected key
        self.assertEqual(storage1.all()[key], base)  # Ensure object is correctly stored

    """
    # Commented-out tests (uncomment if needed)
    
    def test_a_all(self):
        \"\"\"
        Test that all() returns an empty dictionary when no objects are stored.
        \"\"\"
        all_objs = storage.all()
        self.assertDictEqual(storage.all(), {})

    def test_z_all(self):
        \"\"\"
        Test that all() returns a dictionary after saving an object.
        \"\"\"
        base = BaseModel()
        base.save()
        key = 'BaseModel.' + base.id
        self.assertIsInstance(storage.all(), dict)

    def test_reload(self):
        \"\"\"
        Test that reload() does not return anything.
        \"\"\"
        self.assertEqual(storage.reload(), None)
    """
