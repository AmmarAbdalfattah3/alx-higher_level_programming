#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) != 'p' or chr(letter) != 'e':
        print("{:c}".format(letter), end="")
