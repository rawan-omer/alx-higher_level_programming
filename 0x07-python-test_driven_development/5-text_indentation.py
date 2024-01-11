#!/usr/bin/python3
"""text_indentation Definition"""


def text_indentation(text):
    """prints a text with 2 new lines after some char"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for t in text:
        if t in ['.', '?', ':']:
            print(line.strip())
            print()
            line = ""

        else:
            line += t

    if (line):
        print(line.strip())
