#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import numpy as np

def main():
    input_file = sys.argv[1]


    list_start = []
    list_end = []
    with open(input_file) as f:
        lines = f.read().splitlines()
        for line in lines:
            start, end = line.split(' -> ')
            list_start.append([int(elem) for elem in start.split(',')])
            list_end.append([int(elem) for elem in end.split(',')])
        list_start = np.array(list_start)
        list_end = np.array(list_end)

        xmax = max(np.concatenate((list_start[:, 0], list_end[:, 0]), axis=None))
        ymax = max(np.concatenate((list_start[:, 1], list_end[:, 1]), axis=None))
        grid = np.zeros((ymax+1, xmax+1), dtype=int)
        print(f"xmax is {xmax}")
        print(f"ymax is {ymax}")
        #grid = np.zeros((10,10), dtype=int)

        for i in range(len(list_start)):
            #print(f"{list_start[i]} -> {list_end[i]}")
            x1, x2 = list_start[i, 0], list_end[i, 0]
            y1, y2 = list_start[i, 1], list_end[i, 1]

            if x1 == x2:
                if y2 < y1:
                    y1, y2 = y2, y1
                grid[y1:y2+1, x1] += 1
                #print(grid)
            elif y1 == y2:
                if x2 < x1:
                    x1, x2 = x2, x1
                grid[y1, x1:x2+1] += 1
                #print(grid)
            else:
                if x1 == y1 and x2 == y2:
                    #print(f"Changes: {list_start[i]} -> {list_end[i,]}")
                    if y2 < y1:
                        y1, y2 = y2, y1
                    if x2 < x1:
                        x1, x2 = x2, x1
                    j = y1
                    k = x1
                    while j < y2+1 and k < x2+1:
                        grid[j][k] += 1
                        #print(f"Add 1 to case {(j, k)}")
                        j += 1
                        k += 1
                    #print(grid)
                elif x1 == y2 and y1 == x2:
                    #print(f"Changes: {list_start[i]} -> {list_end[i,]}")
                    if y1 < x1:
                        assert(y1 < y2)
                        assert(x1 > x2)
                        j = y1
                        k = x1
                        while j < y2+1 and k > x2-1:
                            #print(f"Add 1 to case {(j, k)}")
                            grid[k][j] += 1
                            j += 1
                            k -= 1
                        #print(grid)
                    if y1 > x1:
                        j = y1
                        k = x1
                        while j > y2-1 and k < x2+1:
                            #print(f"Add 1 to case {(j, k)}")
                            grid[k][j] += 1
                            j -= 1
                            k +=1
                        #print(grid)
                elif abs(x1-x2) == abs(y1-y2):
                    j = y1
                    k = x1
                    if y1 < y2:
                        if x1 < x2:
                            while j < y2+1 and k < x2+1:
                                grid[j][k] +=1
                                j += 1
                                k += 1
                        if x2 < x1:
                            while j < y2+1 and k > x2-1:
                                grid[j][k] += 1
                                j+=1
                                k-=1
                    elif y1 > y2:
                        if x1 < x2:
                            while j > y2-1 and k < x2+1:
                                grid[j][k] +=1
                                j -= 1
                                k += 1
                        if x2 < x1:
                            while j > y2-1 and k > x2-1:
                                grid[j][k] += 1
                                j-=1
                                k-=1
                        pass
                    pass
        print(grid)
        grid = np.where(grid<2, 0, grid)
        grid = np.where(grid>=2, 1, grid)
        nb_two = np.sum(grid)
        #grid[1:8][2:9]+=1
        print(f"xmax is {xmax}")
        print(f"ymax is {ymax}")
        #print(grid[1:10][1:10])
        print(f"There are {nb_two} points where there are more than 2 crossing lines.")


if __name__ == '__main__':
    main()
