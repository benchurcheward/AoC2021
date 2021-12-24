#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from statistics import median

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        pos = [int(p) for p in next(f).split(',')]

    #puzzle1
    median_pos = median(pos)
    fuel = [abs(median_pos-x) for x in pos]
    print(sum(fuel))

    return

if __name__ == '__main__':
    main()
