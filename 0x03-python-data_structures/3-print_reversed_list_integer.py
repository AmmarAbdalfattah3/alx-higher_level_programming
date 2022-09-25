#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list.copy()
    for item in reversed(range(len(rev_list))):
        print("{:d}".format(rev_list[item]))
