#!/usr/bin/python3
"""Module that prints a first and last name."""


def say_my_name(first_name, last_name=""):
    """Prints a first and last name.
    Args:
        first_name (str): The first name.
        last_name (str): The last name.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
