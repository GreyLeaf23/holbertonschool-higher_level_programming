#!/usr/bin/python3
if __name__ == "__main__":
    import sys

argument = len(sys.argv) - 1
num_arguments = argument

if num_arguments == 0:
        print("0 arguments.")

elif num_arguments == 1:
     print("1 argument:")

else:
    print("{} arguments:".format(num_arguments))

for i in range(num_arguments):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))

