#!/usr/bin/python3
def no_c(my_string):
    new_string = ''

    for c_char in my_string:
        if c_char not in ['c', 'C']:
            new_string += c_char

    return new_string
