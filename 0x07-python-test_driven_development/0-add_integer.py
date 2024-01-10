#!/usr/bin/python3
''' Function that add 2 numbers '''


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    b = int(b)
    a = int(a)

    return (a + b)
