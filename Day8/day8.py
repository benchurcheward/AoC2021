#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def function(arg):
    return


def main():
    input_file = sys.argv[1]

    digits = [0]*10

    #puzzle1
    with open(input_file) as f:
        while(line := next(f, None)) is not None:
            output_values = line.split(' | ')[1]
            for word in output_values.split(' '):
                if len(word) == 2:
                    digits[1] +=1
                elif len(word) == 3:
                    digits[7] += 1
                elif len(word) == 4:
                    digits[4] += 1
                elif len(word) == 7:
                    digits[8] += 1
    print(sum(digits))

if __name__ == '__main__':
    main()
