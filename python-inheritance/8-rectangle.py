#!/usr/bin/python3
""""
Module contains a class named Rectangle, which inherits
from BaseGeometry class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Creates a class named Rectangle, which inherits
    from BaseGeometry class.
    """
    def __init__(self, width, height):
        """Initializes an instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
