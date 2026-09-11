#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_init_no_args(self):
        """Test instantiation with no arguments."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test instantiation with kwargs."""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)

    def test_str_representation(self):
        """Test string output format."""
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save(self):
        """Test save method updates timestamp."""
        model = BaseModel()
        old_time = model.updated_at
        model.save()
        self.assertNotEqual(old_time, model.updated_at)

    def test_to_dict(self):
        """Test to_dict method produces correct dict."""
        model = BaseModel()
        d = model.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
