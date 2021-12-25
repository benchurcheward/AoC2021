#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        lines = f.read().splitlines()
        low_points = []
        #lines = [(l1, l2, l3) for (l1, l2, l3) in zip(lines, lines[1:], lines[2:])]
        for i in range(len(lines)):
            if i == 0:
                #first line
                line = [int(e) for e in lines[i]]
                line_next = [int(e) for e in lines[i+1]]
                for j in range(len(line)):
                    if j == 0:
                        if line[j] < line[j+1] and line[j] < line_next[j]:
                            low_points.append(line[j])
                    elif j == len(line) - 1:
                        if line[j] < line[j-1] and line[j] < line_next[j]:
                            low_points.append(line[j])
                    else:
                        if line[j] < line[j+1] and line[j] < line[j-1] and line[j] < line_next[j]:
                            low_points.append(line[j])

            elif i == len(lines) - 1:
                #last line
                line_prev = [int(e) for e in lines[i-1]]
                line = [int(e) for e in lines[i]]
                for j in range(len(line)):
                    if j == 0:
                        if line[j] < line[j+1] and line[j] < line_prev[j]:
                            low_points.append(line[j])
                    elif j == len(line) - 1:
                        if line[j] < line[j-1] and line[j] < line_prev[j]:
                            low_points.append(line[j])
                    else:
                        if line[j] < line[j+1] and line[j] < line[j-1] and line[j] < line_prev[j]:
                            low_points.append(line[j])

            else:
                line_prev = [int(e) for e in lines[i-1]]
                line = [int(e) for e in lines[i]]
                line_next = [int(e) for e in lines[i+1]]
                for j in range(len(line)):
                    if j == 0:
                        if line[j] < line[j+1] and line[j] < line_prev[j] and line[j] < line_next[j]:
                            low_points.append(line[j])
                    elif j == len(line) - 1:
                        if line[j] < line[j-1] and line[j] < line_prev[j] and line[j] < line_next[j]:
                            low_points.append(line[j])
                    else:
                        if line[j] < line[j+1] and line[j] < line[j-1] and line[j] < line_prev[j] and line[j] < line_next[j]:
                            low_points.append(line[j])

    risk = sum(low_points) + len(low_points)
    print(f"The sum of risks is {risk}.")

if __name__ == '__main__':
    main()
