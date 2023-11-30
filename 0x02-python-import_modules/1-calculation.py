#!/usr/bin/python3
from calculator_1 import add, sub, mal, div
if __name__ = "__main__":
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mal(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
