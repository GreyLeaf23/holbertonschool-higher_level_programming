#!/usr/bin/python3
"""Module that creates an Object from a “JSON file”."""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
