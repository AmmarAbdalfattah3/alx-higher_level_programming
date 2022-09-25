#!/usr/bin/python3
if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
