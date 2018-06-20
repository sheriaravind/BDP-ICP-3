#!/usr/bin/env python

import sys

def Input_Data():
    for line in sys.stdin:
        matrix, row, col, val = line.strip().split(",")
        list = [matrix, row, col]
        print("{0}\t{1}".format(list, val))

if __name__ == '__main__':
    Input_Data()