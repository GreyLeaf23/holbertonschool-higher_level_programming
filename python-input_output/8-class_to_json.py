#!/usr/bin/python3
"""
Module writes a function that returns dictionary description
with simple data struture.
"""


def class_to_json(obj):
    """
    Returns simple data structure (list, dictionary, string)
    for JSON serialization.
    """
    return obj.__dict__
