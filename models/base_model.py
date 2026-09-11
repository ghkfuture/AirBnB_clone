#!/usr/bin/python3
"""
BaseModel class module.
Defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines common attributes and methods for future subclasses."""

    def __init__(self, *args, **kwargs):
        """Initialize attributes for BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        val = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                        setattr(self, key, val)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return official string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at with the current datetime and save instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation containing key-values of instance."""
        res = self.__dict__.copy()
        res["__class__"] = self.__class__.__name__
        res["created_at"] = self.created_at.isoformat()
        res["updated_at"] = self.updated_at.isoformat()
        return res
