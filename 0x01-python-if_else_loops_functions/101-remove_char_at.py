#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
    del_char = str[:n] + str[n+1:]
        return del_char
    else:
        return str
