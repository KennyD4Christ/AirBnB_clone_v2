#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel  # noqa F184
from models.amenity import Amenity  # noqa F184
from models.city import City  # noqa F184
from models.place import Place  # noqa F184
from models.review import Review  # noqa F184
from models.state import State  # noqa F184
from models.user import User  # noqa F184


class FileStorage:
    """Represent an abstracted storage engine.


    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects.

        If a cls is specified, returns a dictionary of objects of that type.
        Otherwise, returns the __objects dictionary.
        """
        if cls is not None:
            if type(cls) is str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) is cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        # Manually manage relationships between State and City objects
        if isinstance(obj, City):
            state_key = "State." + obj.state_id
            state = self.__objects.get(state_key)
            if state:
                state.cities.append(obj)
        elif isinstance(obj, State):
            for city in obj.cities:
                city.state_id = obj.id
                self.new(city)

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = {}
        for key, obj in self.__objects.items():
            # Check if the object is of type City
            if isinstance(obj, City):
                # Exclude non-serializable attributes
                city_dict = obj.__dict__.copy()
                city_dict.pop('_sa_instance_state', None)
                odict[key] = city_dict
            else:
                # For other objects, use the existing to_dict() method
                odict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f, default=str)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                # Manually manage relationships
                if isinstance(obj, City):
                    state_key = "State." + obj.state_id
                    state = self.__objects.get(state_key)
                    if state and obj in state.cities:
                        state.cities.remove(obj)

    def close(self):
        """Call the reload method."""
        self.reload()
