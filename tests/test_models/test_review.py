#!/usr/bin/python3
"""
Unit test suite for the Review model, which inherits from BaseModel.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the Review model.
    """

    def test_str(self):
        """
        Test default attribute values of the Review model.
        Ensures that attributes are initialized with the correct default values:
        - Strings should be empty ("")
        """
        review = Review()
        self.assertEqual(review.place_id, "")  # Place ID should be an empty string
        self.assertEqual(review.user_id, "")  # User ID should be an empty string
        self.assertEqual(review.text, "")  # Review text should be an empty string

    def test_parent(self):
        """
        Test inheritance from BaseModel.
        Verifies that an instance of Review is also an instance of BaseModel.
        """
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))  # Confirm Review inherits from BaseModel