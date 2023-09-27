#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s_str = f"Last digit of {number}"
l_digit = int(str(number)[-1:])

if number < 0:
    l_digit = -l_digit

if l_digit > 5:
    print("{} is {} and is greater than 5".format(s_str, l_digit))

elif l_digit == 0:
    print("{} is {} and is 0".format(s_str, l_digit))

else:
    print("{} is {} and is less than 6 and not 0".format(s_str, l_digit))
