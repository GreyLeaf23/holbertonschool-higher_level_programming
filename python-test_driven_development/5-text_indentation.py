#!/usr/bin/python3
"""Module to print a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints 2 new lines after
    specified characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.replace(". ", ".\n\n")
        text = text.replace("? ", "?\n\n")
        text = text.replace(": ", ":\n\n")
        print(text, end="")
