#!/usr/bin/python3
"""Module creates class name Student."""


class Student():
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a
        student.
        """
        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dict[att] = self.__dict__[att]
            return dict
