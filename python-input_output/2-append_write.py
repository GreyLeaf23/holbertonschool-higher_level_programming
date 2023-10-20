#!/usr/bin/python3
"""Module that apeends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns the
    number of characters added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
