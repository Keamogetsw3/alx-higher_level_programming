#!/usr/bin/python3
"""
Unit tests for the Amenity class.

This module contains test cases to verify the functionality of the 
Amenity class, ensuring it behaves as expected.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestBaseModel(unittest.TestCase):
    """
    Defines test cases for the Amenity class.
    """

    def test_str(self):
        """
        Test that the 'name' attribute of an Amenity instance 
        is initialized as an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_parent(self):
        """
        Test that an Amenity instance is correctly inherited 
        from the BaseModel class.
        """
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))