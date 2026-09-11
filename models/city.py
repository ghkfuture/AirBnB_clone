#!/usr/bin/python3
"""City class module."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class representing cities in a state."""
    state_id = ""
    name = ""
