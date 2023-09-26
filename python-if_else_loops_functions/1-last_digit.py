#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
start_str = "Last digit of {number}"
if number > 0:
    print("{start_str} is {} and is greater than 5".format(number, number))

if number == 0:
    print("{start_str} is {} and is 0".format(number, number))

if number < 0:
    print("{start_str} is {} and is less than 6 and not 0".format(number, number))
