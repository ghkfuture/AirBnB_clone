#!/usr/bin/python3
"""
Module for FileStorage class.
Handles JSON serialization and deserialization of objects.
"""
import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes the JSON file to __objects if file exists."""
        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }

        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value.get("__class__")
                        if cls_name in classes:
                            FileStorage.__objects[key] = (
                                classes[cls_name](**value)
                            )
            except Exception:
                pass
