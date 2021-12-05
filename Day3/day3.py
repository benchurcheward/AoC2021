#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def gamma_epsilon(list_bits):
    """
    Iterate through a list of lines of bits.
    Computes gamma rate and epsilon rate, encoding as lines of bits:
    Bits of gamma are the most common bits at each position.
    Bits of espilon are the least common bits at each position.

    Returns product of gamma and epsilon. O(3n)
    """

    n = len(list_bits)
    counts  = [0]*len(list_bits[0])
    gamma   = [0]*len(list_bits[0])
    epsilon = [0]*len(list_bits[0])
    gamma_rate = 0
    epsilon_rate = 0

    for binary in list_bits:
        #binary = binary.split()
        for i in range(len(binary)):
            counts[i] += int(binary[i])

    for i in range(len(counts)):
        #counts[i] represent the number of 1 at ith position
        #if > n/2, then 1 is more common
        #put sup or equal as there is no clue to manage equalities
        if counts[i] >= n/2:
            gamma[i] = 1
            epsilon[i] = 0
        else:
            gamma[i] = 0
            epsilon[i] = 1
    for i in range(len(gamma)):
        #in python list index increase from left to right
        #so we need to inverse position for the decimal conversion
        if gamma[len(gamma)-i-1] == 1:
            #** is the power operator
            gamma_rate += 2**i
        if epsilon[len(gamma)-i-1] == 1:
            epsilon_rate += 2**i

    return gamma_rate * epsilon_rate


def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        list_bits = f.read().splitlines()
        power_consumption = gamma_epsilon(list_bits)

    print(f'This is the power_consumption: {power_consumption}')
    return

if __name__ == '__main__':
    main()
