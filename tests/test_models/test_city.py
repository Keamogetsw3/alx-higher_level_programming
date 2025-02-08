#!/usr/bin/python3
"""
Unit test suite for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class and its attributes.
    """

    def test_attr(self):
        """
        Test default attributes of the City model.
        Ensures that 'state_id' and 'name' are initialized as empty strings.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_parent(self):
        """
        Test inheritance from BaseModel.
        Verifies that an instance of City is also an instance of BaseModel.
        """
        city = City()
        self.assertTrue(isinstance(city, BaseModel))