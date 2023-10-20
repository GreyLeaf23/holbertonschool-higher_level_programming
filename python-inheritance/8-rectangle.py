#!/usr/bin/python3
""""
Module contains a class named Rectangle, which inherits
from BaseGeometry class.
"""


class BaseGeometry:
    """
    Defines a BaseGeometry class.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
    """

    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
            width (int): private
            height (int): private
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
