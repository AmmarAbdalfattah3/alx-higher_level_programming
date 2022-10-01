#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = 0
    for item in set(my_list):
        uniq_int += item
    return uniq_int
