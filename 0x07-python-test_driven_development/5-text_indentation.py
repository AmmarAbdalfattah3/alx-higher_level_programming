#!/usr/bin/python3
"""This module prints a text with 2 new lines
   after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): is a string.
    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
