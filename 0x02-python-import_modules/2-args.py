#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv) - 1
    x = 0
    if len_argv == 1:
        print("{:d} argument:".format(len_argv))
    else:
        print("{:d} arguments:".format(len_argv))
    for string in argv:
        if string != argv[0]:
            x += 1
            print("{:d}: {:s}".format(x, string))
