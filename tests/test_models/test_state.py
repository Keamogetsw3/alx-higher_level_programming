#!/usr/bin/python3
"""
Unit test suite for the State model, which inherits from BaseModel.
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the State model.
    """

    def test_attr(self):
        """
        Test default attribute values of the State model.
        Ensures that the 'name' attribute is initialized as an empty string.
        """
        state = State()
        self.assertEqual(state.name, "")  # Name should be an empty string

    def test_parent(self):
        """
        Test inheritance from BaseModel.
        Verifies that an instance of State is also an instance of BaseModel.
        """
        state = State()
        self.assertTrue(isinstance(state, BaseModel))  # Confirm State inherits from BaseModel