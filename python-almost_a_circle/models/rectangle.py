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
        if args and len(args) != 0:
            for item in range(len(args)):
                if item == 0:
                    self.id = args[item]
                if item == 1:
                    self.width = args[item]
                if item == 2:
                    self.width = args[item]
                if item == 3:
                    self.x = args[item]
                if item == 4:
                    self.y = args[item]
            else:
                for kw in kwargs:
                    if kw == "id":
                        self.id = (kwargs[kw])
                    if kw == "width":
                        self.width = (kwargs[kw])
                    if kw == "height":
                        self.height = (kwargs[kw])
                    if kw == "x":
                        self.x = (kwargs[kw])
                    if kw == "y":
                        self.y = (kwargs[kw])

    def to_dictionary(self):
        """Returns Rectangle as dictionary."""
        attr_list = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attr_list}
