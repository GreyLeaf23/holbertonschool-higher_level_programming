#!/usr/bin/python3
"""Module that writes an object to a text file, using a
 JSON representation"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file."""
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
