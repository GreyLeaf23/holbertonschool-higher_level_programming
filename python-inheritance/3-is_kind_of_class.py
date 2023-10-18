#!/usr/bin/python3
"""
Module returns true or false if the object is an
instance of a class that inherited (directly or
indirectly).
"""


def is_kind_of_class(obj, a_class):
    """Returns true or false if the object is an
    instance of a class that inherited (directly or
    indirectly).
    Args:
        obj: object to check
        a_class: class to check against
    Return:
        True if the object is an instance of a class that
        inherited (directly or indirectly) from the
        specified class, otherwise False
    """
    return isinstance(obj, a_class)
