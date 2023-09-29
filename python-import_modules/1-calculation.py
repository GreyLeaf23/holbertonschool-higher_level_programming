#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Using 'add' function from module.
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Using 'sub' function from module.
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Using 'mul' function from module.
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Using 'div' function from module.
    print("{} / {} = {}".format(a, b, div(a, b)))
