#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import math

def parse_grid(input_file):
    with open(input_file) as f:
        #ugly, but to have only two arguments fro get_adjacents
        global grid
        grid = [[int(e) for e in line] for line in f.read().splitlines()]

def get_adjacents(i, j):
    adjacents = []
    if i < len(grid[i])-1:
        adjacents.append(grid[i+1][j])
    if i > 0:
        adjacents.append(grid[i-1][j])
    if j < len(grid[i])-1:
        adjacents.append(grid[i][j+1])
    if j > 0:
         adjacents.append(grid[i][j-1])
    return adjacents

def check_surface(i,j):
    count = 0

    if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] != 9:
        #we don't want to count the cell again
        grid[i][j] = 9
        count += 1
    else:
        return 0

    for di, dj in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
        count += check_surface(i+di, j+dj)

    return count

def main():

    input_file = sys.argv[1]

    parse_grid(input_file)
    low_points = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacents = get_adjacents(i, j)
            if grid[i][j] < min(adjacents):
                low_points.append(grid[i][j])
    sum_risk = sum(low_points) + len(low_points)

    print(f"The sum of risks is {sum_risk}.")

    #2
    surfaces = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            surfaces.append(check_surface(i, j))
    final_product = math.prod(sorted(surfaces)[-3:])
    print(f"Product of the three largest surfaces is {final_product}.")

if __name__ == '__main__':
    main()
