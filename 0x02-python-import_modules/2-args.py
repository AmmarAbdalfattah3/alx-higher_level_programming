#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_argv = len(argv)
    x = 0
    if len_argv > 1:
        print("{:d} arguments:".format(len_argv - 1))
    else:
        print("{:d} argument:".format(len_argv - 1))
    for i in argv:
        if i != argv[0]:
            x += 1
            print("{:d}: {:s}".format(x, i))
