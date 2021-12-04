#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

#test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def read_depths(input_file):
    """
    Simple: read the file, iterates through the list of lines.
    """
    with open(input_file) as f:
        count = 0
        #file lines are str
        #if we don't change them into int, we'd miss one increase
        previous = int(f.readline())
        #splitlines removes the endline character '\n'
        depths = f.read().splitlines()
        for depth in depths:
            depth = int(depth)
            if depth > previous:
                count += 1
            else:
                pass
            #upload the previous value
            previous = depth
    return count

def read_depths_2(input_file):
    """
    Avoid to load the whole file into a list to save memory.
    """
    with open(input_file) as f:
        count = 0
        #return the next element of iterator f
        #split removes the endline character '\n'
        previous = int(next(f).strip())
        while True:
            try:
                depth = int(next(f).strip())
                if depth > previous:
                    count += 1

                previous = depth
            except StopIteration:
                #will trigger after reaching the last element
                break
    return count

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

    count_increase = read_depths(input_file)

    print(f'There are {count_increase} measurements larger than the precedent.')
    count_increase = read_depths_2(input_file)
    print(f'There are {count_increase} measurements larger than the precedent.')
    count_increase = sliding_window(input_file, 3)
    print(f'There are {count_increase} measurements larger than the precedent.')
    return

if __name__ == '__main__':
    main()
