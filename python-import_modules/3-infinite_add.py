#!/usr/bin/python3
if __name__ == "__main__":
    import sys

add = 0
result = 0
argument = len(sys.argv) - 1

for i in range(argument):
    add = add + 1
    result = int(result) + int(sys.argv[add])
print("{}".format(result))
