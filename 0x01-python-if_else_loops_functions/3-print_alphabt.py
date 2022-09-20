#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    char = "{:c}".foramt(letter)
    if char != 'p' or char != 'e':
        print("{:c}".format(letter), end="")
