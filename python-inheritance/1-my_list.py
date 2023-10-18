#!/usr/bin/python3
"""Module inherits attributes and methods from list"""


class MyList(list):
    """Class inherits attributes and methods from
    list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
