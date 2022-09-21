#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    letter1 = chr(letter - 32)
    letter2 = chr(letter)
    char = "{:s}".format(letter1 if letter % 2 != 0 else letter2)
    print(char, end="")
