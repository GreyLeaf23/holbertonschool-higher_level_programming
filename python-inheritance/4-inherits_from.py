#!/usr/bin/python3
"""
Module returns true or false if the object is an
instance of a class that inherited (directly or
indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns true or false if the object is an
    instance of a class that inherited (directly or
    indirectly) from the specified class.
    Args:
        obj: object to check
        a_class: class to check against
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
