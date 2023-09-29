#!/usr/bin/python3
#Importing function from 'add_0.py' file/module.
if __name__ is "__main__":

    from add_0 import add

    a = 1
    b = 2

    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
