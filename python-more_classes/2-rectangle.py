#!/usr/bin/python3
"""
Module that defines a rectangle by width and height.
"""


class Rectangle:
    """Defines class rectangle with private attributes width and height.

    Methods:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height
        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


def area(self):
    """Returns area of rectangle."""
    return self.__width * self.__height


def perimeter(self):
    """Returns perimeter of rectangle."""
    if self.__width == 0 or self.__height == 0:
        return 0
    return 2 * (self.__width + self.__height)
