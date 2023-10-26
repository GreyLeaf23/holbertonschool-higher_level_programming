#!/usr/bin/python3
"""Module defines a class named Rectangle."""


from models.base import Base


class Rectangle(Base):
    """Creating class Rectangle with its dimensional elements."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Dimensional elements of Rcetangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets private attribute - Width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets private attribute - Width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets private attribute - Height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets private attribute - Height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets private attribute - X."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets private attribute - X."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets private attribute - Y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets private attribute - X."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Rectangle Area"""
        return self.__width * self.__height

    def display(self):
        """Displays Rectangle."""
        for ver in range(self.__y):
            print("")
        for hor in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Overrides method so it returns specified value.
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute."""
        attr_list = ["id", "width", "height", "x", "y"]
        if args:
            for item in range(len(args)):
                setattr(self, attr_list[item], args[item])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns Rectangle as dictionary."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
