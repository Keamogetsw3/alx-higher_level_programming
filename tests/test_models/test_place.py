#!/usr/bin/python3
"""
Unit test suite for the Place model, which inherits from BaseModel.
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the Place model.
    """

    def test_str(self):
        """
        Test default attribute values of the Place model.
        Ensures that attributes are initialized with the correct default values:
        - Strings should be empty ("")
        - Integers should be 0
        - Floats should be 0.0
        - Lists should be empty ([])
        """
        place = Place()
        self.assertEqual(place.city_id, "")  # City ID should be an empty string
        self.assertEqual(place.user_id, "")  # User ID should be an empty string
        self.assertEqual(place.name, "")  # Place name should be an empty string
        self.assertEqual(place.description, "")  # Description should be an empty string
        self.assertEqual(place.number_rooms, 0)  # Number of rooms should be 0
        self.assertEqual(place.number_bathrooms, 0)  # Number of bathrooms should be 0
        self.assertEqual(place.max_guest, 0)  # Max guest capacity should be 0
        self.assertEqual(place.price_by_night, 0)  # Price per night should be 0
        self.assertEqual(place.latitude, 0.0)  # Latitude should be 0.0
        self.assertEqual(place.longitude, 0.0)  # Longitude should be 0.0
        self.assertEqual(place.amenity_ids, [])  # Amenity IDs should be an empty list

    def test_parent(self):
        """
        Test inheritance from BaseModel.
        Verifies that an instance of Place is also an instance of BaseModel.
        """
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))  # Confirm Place inherits from BaseModel