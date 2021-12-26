#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import numpy as np

def parse_grid(input_file):
    with open(input_file) as f:
        grid = np.array([np.array([int(i) for i in l], dtype=int) for l in f.read().splitlines()], dtype=int)
    return grid

def get_adjacents(grid, i, j):
    adjacents = []
    if i+1 < len(grid):
        adjacents.append((i+1, j))
        if j+1 < len(grid[i]):
            adjacents.append((i+1, j+1))
        if j > 0:
            adjacents.append((i+1,j-1))
    if i > 0:
        adjacents.append((i-1, j))
        if j > 0:
            adjacents.append((i-1, j-1))
        if j+1 < len(grid[i]):
            adjacents.append((i-1, j+1))
    if j+1 < len(grid[i]):
        adjacents.append((i, j+1))
    if j > 0:
        adjacents.append((i, j-1))
    return adjacents

def flash(grid, i, j):
    count = 0
    grid[i][j] += 1
    if grid[i][j] == 10:
        count += 1
        for x, y in get_adjacents(grid, i, j):
            count += flash(grid, x, y)
    else:
         return 0
    return count

def main():

    input_file = sys.argv[1]
    grid = parse_grid(input_file)
    #print(grid)
    count_flash = 0
    t = 0
    while True:
        t += 1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count_flash += flash(grid, i, j)
        grid = np.where(grid>9, 0, grid)
        if np.sum(grid) == 0:
            print(f"All octopus flash at once during {t}-th step.")
            break
        if t == 100:
            print(f"There have been {count_flash} flashes after 100 steps.")
    return

if __name__ == '__main__':
    main()
