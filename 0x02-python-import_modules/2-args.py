#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    args = argv[1:]

    print("{} argument{}:".format(argc, 's' if argc != 1 else ''))
    if argc == 0:
        print(".")
    else:
        for r, arg in enumerate(args, start=1):
            print("{}: {}".format(r, arg))
