#!/usr/bin/python3
if __name__ == "__main__":
#Importing function from 'add_0.py' file/module.
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)

    print("{} + {} = {}".format(a, b, result))
