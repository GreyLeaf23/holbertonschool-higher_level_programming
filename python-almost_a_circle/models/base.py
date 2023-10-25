#!/usr/bin/python3
"""
Module defines a class named Base and works as the foundation for the project.
"""


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
