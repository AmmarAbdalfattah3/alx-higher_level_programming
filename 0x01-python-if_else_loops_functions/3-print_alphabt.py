#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
char = "{:c}".format(letter)
    if char != 'p' or char != 'e':
        print(char, end="")
