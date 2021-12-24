#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from statistics import median

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        pos = [int(p) for p in next(f).split(',')]

    #pos = [16,1,2,0,4,2,7,1,2,14]
    #puzzle1
    median_pos = median(pos)
    fuel = [abs(median_pos-x) for x in pos]
    print(sum(fuel))

    #puzzle2
    avg = sum([x/len(pos) for x in pos])
    avg = round(avg)-1
    fuel = [abs(avg-x)*(1+abs(avg-x))/2 for x in pos]
    print(sum(fuel))
    return

if __name__ == '__main__':
    main()
