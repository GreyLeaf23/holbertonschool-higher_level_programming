#!/usr/bin/python3
def unqi_add(my_list=[]):
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return sum(new_list)
