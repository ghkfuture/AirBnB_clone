#!/usr/bin/python3
"""BaseModel module for AirBnB clone."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all models in the project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, tformat))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update updated_at and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of instance."""
        r_dict = self.__dict__.copy()
        r_dict["__class__"] = self.__class__.__name__
        r_dict["created_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        return r_dict

    def __str__(self):
        """Return string representation."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
