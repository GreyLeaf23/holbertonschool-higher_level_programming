#!/usr/bin/python3
"""Module that defines a rectangle by width and height."""


class Rectangle:
    """Defines class rectangle with private attributes width and height.
    Methods:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle.
        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        Increments number_of_instances by 1."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted.
        Decrements number_of_instances by 1."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.
        Returns:
            int: The area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.
        Returns:
            int: The perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        new_str = "\n".join([str(self.print_symbol) * self.__width
                            for rows in range(self.__height)])
        return new_str

    def __repr__(self):
        """Returns a string representation of the rectangle that can be used
        to recreate the object."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
