#!/usr/bin/python3
"""Defining a class named Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        """Start new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Define square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value
