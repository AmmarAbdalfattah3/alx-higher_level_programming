#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = 0
    for string in argv[1:]:
        number += int(string)
    print("{:d}".format(number))
