#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        m = f.readlines()
        #Puzzle1
        count_increase = sum([1 for (m1, m2) in zip(m, m[1:]) if m2 > m1])
        #Puzzle2
        count_sliding = sum([1 for (m1,m2,m3,m4) in zip(measures, m[1:], m[2:], m[3:]) if sum((m2,m3,m4)) > sum((m1,m2,m3))])

    print(f'There are {count_increase} measurements larger than the precedent.')
    print(f'There are {count_sliding} triplets larger than the precedent.')

if __name__ == '__main__':
    main()
