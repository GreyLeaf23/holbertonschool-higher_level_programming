#!/usr/bin/python3
"""
Module defines a class named Base and works as the foundation for the project.
"""


import json


class Base:
    """Creation class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method initializes objects with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Converts JSON string to a regular file."""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representing list of dictionaries."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            dummy = cls(1, 0, 0)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as f:
                objs = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in objs]
        except FileNotFoundError:
            return []
