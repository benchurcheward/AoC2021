#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        lanternfish = [int(n) for n in next(f).split(',')]

    lanternfish = [lanternfish.count(x) for x in range(9)]

    for d in range(256):
        new_fishes = lanternfish[0]
        lanternfish = [lanternfish[x+1] if x<8 else lanternfish[0] for x in range(9)]
        lanternfish[6] += new_fishes

    print(sum(lanternfish))


    return

if __name__ == '__main__':
    main()
