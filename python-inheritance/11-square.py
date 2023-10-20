#!/usr/bin/python3
""" This module have class called Rectangle that inherits from BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size):
        """ Function that validates the size """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area """
        return self.__size * self.__size

    def __str__(self):
        """Returns the following square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
