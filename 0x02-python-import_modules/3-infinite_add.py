#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    s = sum(map(int, args)) if args else 0
    print(s)
