#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list
    new_list = my_list.copy()
    for item in range(len(new_list)):
        if item == idx:
            new_list[item] = element
            return new_list
