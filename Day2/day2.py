#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def multiply_pos(list_moves):
    """
    Iterate through a list containing change of submarine position:
    'forward X' move sub horizontaly by X;
    'down X' increases sub's depth by X;
    'up X' decreases sub's depth by X.
    Then returns multiplication of the two coordinates.

    Simplification compared to day1. We iterate through a list.
    """
    horizontal = 0
    depth = 0

    for move in list_moves:

        direction, increment = move.split(' ')
        increment = int(increment)
        #recognize only the first char to save time
        if direction[0] == 'f':
            horizontal += increment
        if direction[0] == 'd':
            depth += increment
        if direction[0] == 'u':
            depth -= increment
        #never encountered, but just in case, for obvious reasons
        if depth < 0:
            depth = 0
    final_pos = horizontal * depth
    #print(f'This is final depth: {depth}')
    #print(f'This is final horizontal: {horizontal}')
    return final_pos

def multiply_pos_with_aim(list_moves):
    """
    This time, add 'aim' parameter. Modifications are as following:
    'down X' increases aim by X;
    'up X' decreases aim by X.
    'forward X' move sub horizontaly by X,
    and increases depth by aim * X.

    Then returns multiplication of the two coordinates.

    Simplification compared to day1. We iterate through a list.
    """

    horizontal = 0
    aim = 0
    depth = 0

    for move in list_moves:

        direction, increment = move.split(' ')
        increment = int(increment)
        #recognize only the first char to save time
        if direction[0] == 'f':
            horizontal += increment
            depth += aim * increment
        if direction[0] == 'd':
            aim += increment
        if direction[0] == 'u':
            aim -= increment
        #never encountered, but just in case, for obvious reasons
        if depth < 0:
            depth = 0
    final_pos = horizontal * depth
    #print(f'This is final depth: {depth}')
    #print(f'This is final horizontal: {horizontal}')
    return final_pos

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        list_moves = f.read().splitlines()
        ##(un)comment the line you want
        #position = multiply_pos(list_moves)
        position = multiply_pos_with_aim(list_moves)
    print(f'Final position is {position}.')
    return

if __name__ == '__main__':
    main()
