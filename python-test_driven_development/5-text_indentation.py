#!/usr/bin/python3
"""Module to print a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
