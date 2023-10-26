#!/usr/bin/python3
"""Module creates class named Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class named Square that inherits aspects of Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Cretes dimensions of the Square."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Gets instance attribute - Size"""
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets instance attribute - Size.
        Uses Width and Height to set it.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides method so it returns specified value.
        [Square] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        """Assigns attributes to arguments."""
        if args:
            attr_list = ["id", "size", "x", "y"]
            for item in range(len(args)):
                setattr(self, attr_list[item], args[item])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns Square as dictionary."""
        attr_list = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attr_list}
