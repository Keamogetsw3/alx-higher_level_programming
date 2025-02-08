#!/usr/bin/python3
"""
Unit test suite for the storage system and BaseModel initialization.
"""

import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """
    Test cases for storage and BaseModel behavior.
    """

    def test_init(self):
        """
        Test the initialization of a BaseModel instance.
        Ensures that the object is correctly created as an instance of BaseModel.
        Also verifies that 'storage' is an instance of FileStorage.
        """
        base = BaseModel()
        self.assertEqual(base.__class__, BaseModel)  # Check if 'base' is a BaseModel instance
        self.assertIsInstance(storage, FileStorage)  # Verify 'storage' is an instance of FileStorage