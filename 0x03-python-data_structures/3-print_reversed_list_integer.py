#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list.copy()
    rev_list.reverse()
    for item in range(len(rev_list)):
        print("{:d}".format(rev_list[item]))
