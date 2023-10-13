#!/usr/bin/python3
"""Defining a class named Rectangle"""


class Rectangle:
    """Create a rectangle with private instance attributes width and height.

    Methods:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)"""

    def __init__(self, width=0, height=0):
        """Constructor for Rectangle class.

        Instantiation with optional width and height"""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Method to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set width"""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
    else:
        self.__width = value

    @property
    def height(self):
        """Method to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set height"""
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError("height must be >= 0")
    else:
        self.__height = value
