#!/usr/bin/python3
"""
Contains tests for FileStorge class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Tests for FileStorage class
    """

    def test_others(self):
        file_path = FileStorage._FileStorage__file_path
        if not os.path.exists(file_path):
            model = BaseModel()
        self.assertTrue(os.path.exists(file_path))


    def test_obj_dict(self):
        model = BaseModel()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_save(self):
        file_path = "file.json"
        fs = FileStorage()
        try:
            os.remove(file_path)
        except:
            pass
        fs.save()
        self.assertTrue(os.path.exists(file_path))
