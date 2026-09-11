#!/usr/bin/python3
"""FileStorage module for JSON serialization and deserialization."""
import json
import os


class FileStorage:
    """Serializes instances to JSON file and deserializes back to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        json_objects = {}
        for key, obj in self.__class__.__objects.items():
            json_objects[key] = obj.to_dict()
        with open(self.__class__.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes JSON file to __objects if file exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if os.path.exists(self.__class__.__file_path):
            try:
                with open(
                    self.__class__.__file_path, "r", encoding="utf-8"
                ) as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value.get("__class__")
                        if cls_name in classes:
                            self.__class__.__objects[key] = (
                                classes[cls_name](**value)
                            )
            except Exception:
                pass
