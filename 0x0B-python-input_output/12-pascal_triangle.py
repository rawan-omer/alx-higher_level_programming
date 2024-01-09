#!/usr/bin/python3
"""pascal_triangle Definition"""


def pascal_triangle(n):
    """returns a list of lists of integers representing Pascal triangle"""
    if n <= 0:
        return []
    tringle = [[1]]

    while len(tringle) != n:
        t = tringle[-1]
        x = [1]
        for i in range(len(t) - 1):
            x.append(t[i] + t[i + 1])
        x.append(1)
        tringle.append(x)
    return tringle
