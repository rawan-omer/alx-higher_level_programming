#!/usr/bin/python3
"""write_file definition"""


def write_file(filename="", text=""):
    """writes string to a text file and returns the number of characters"""
    with open(filename, "w", encoding='utf-8') as f:
        return len(list(f))
