#!/usr/bin/python3
"""
Module contains a function that returns true or
false if the object is exactly an instance of the
specified class.
"""


def is_same_class(obj, a_class):
    """Returns true or false if the object is exactly
    an instance of the specified class.
    Args:
        obj: object to check
        a_class: class to check against
    """
    return type(obj) is a_class
