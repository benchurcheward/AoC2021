#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

#test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def sliding_window(input_file, width):
    """
    Avoid to load the whole file into a list to save memory.
    Width is customizable, but the exercise needs width = 3.
    """
    with open(input_file, 'r') as f:
        count = 0
        #return the next element of iterator f
        #split removes the endline character '\n'
        first  = int(next(f).strip())
        second = int(next(f).strip())
        third  = int(next(f).strip())
        prevdepth = first + second + third

        while True:
            try:
                #upload the values
                #as it is a sliding window, only the third is new
                #and needs to be read from f
                first  = second
                second = third
                third  = int(next(f).strip())

                depth = first + second + third

                if depth > prevdepth:
                    count += 1
                prevdepth = depth

            except StopIteration:
                #will trigger after reaching the last element
                break
    return count

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        m = f.readlines()
        count_increase = sum([1 for (m1, m2) in zip(m, m[1:]) if m2 > m1])

    print(f'There are {count_increase} measurements larger than the precedent.')
    #count_increase = read_depths_2(input_file)
    #print(f'There are {count_increase} measurements larger than the precedent.')
    count_sliding = sliding_window(input_file, 3)
    print(f'There are {count_sliding} measurements larger than the precedent.')
    return

if __name__ == '__main__':
    main()
