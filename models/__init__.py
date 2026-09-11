"""
Initialize the models package and set up storage.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
