#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new() adds an object to __objects."""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test save() creates file and reload() loads objects."""
        model = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        self.storage.reload()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
