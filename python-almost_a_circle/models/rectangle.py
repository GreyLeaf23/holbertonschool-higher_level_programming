#!/usr/bin/python3
"""Module defines a class named Rectangle."""

from models.base import Base


class Rectangle(Base):
    """Creating class Rectangle with its dimensional elements."""

def __init__(self, width, height, x=0, y=0, id=None)
    """Dimensional elements of Rcetangle."""
    super().__init__(id)
    self.width = width
    self.height = height
    self.x = x
    self.y = y
