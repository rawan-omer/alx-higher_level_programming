#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        n = 1
        for i in row:
            if n == len(row):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            n += 1
        print()
