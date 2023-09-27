#!/usr/bin/python3
def uppercase(str):
	for upper in str:
		if upper >= chr(97) and upper <= chr(122):
			upper = chr(ord(upper) - 32)
		print("{}".format(upper), end="")
	print("")