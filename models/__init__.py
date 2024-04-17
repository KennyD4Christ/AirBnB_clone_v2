#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.state import State  # noqa F184
from models.city import City  # noqa F184
from models.engine.file_storage import FileStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
