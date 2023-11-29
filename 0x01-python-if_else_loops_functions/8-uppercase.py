#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        r = ord(str[i])
        if r >= 97 and r < 123:
            r = r - 32
        print("{}".format(chr(r)), end="")
    print()
