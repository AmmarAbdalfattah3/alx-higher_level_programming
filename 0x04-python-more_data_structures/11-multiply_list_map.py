#!/usr/bin/python3
def multiply_list_imap(my_list=[], number=0):
    new_list = list(map(lambda item: item * number, my_list))
    return new_list
