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

    def my_print(self):
        """Print square"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)

    @property
    def position(self):
        """Get square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position"""

        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value
