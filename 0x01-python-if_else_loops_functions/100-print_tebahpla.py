#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{:s}".format(chr(letter - 32) if letter % 2 != 0 else chr(letter)), end="")
