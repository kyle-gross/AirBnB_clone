#!/usr/bin/python3
"""
Module for class FileStorage
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file
    Deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the OBJ with key <obj class name>.id
        """
        new_obj = obj.to_dict()
        new_key = type(obj).__name__
        new_key += "." + obj.id
        FileStorage.__objects[new_key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file(path:__file_path)
        """
        dict2 = {}
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            for key, value in FileStorage.__objects.items():
                dict2[key] = value.to_dict()
            json.dump(dict2, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        Only if the JSON file __file_path exists
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                temp_objs = json.load(f)
            for k, v in temp_objs.items():
                FileStorage.__objects[k] = BaseModel(**v)
