#!/usr/bin/python3
"""This module contains the append_write function"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
