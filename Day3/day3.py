#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def gamma_epsilon(list_bits):
    """
    Computes gamma rate and epsilon rate, encoding as lines of bits:
    Bits of gamma are the most common bits at each position.
    Bits of espilon are the least common bits at each position.

    Returns product of gamma and epsilon.
    """

    n = len(list_bits)
    k = len(list_bits[0])-1
    counts  = [0]*len(list_bits[0])
    gamma = 0
    epsilon = 0

    counts = [sum(bit) for bit in zip(*list_bits)]

    for i in range(len(counts)):
        #most common = 1
        if counts[i] >= n/2:
            gamma += 1 << k-i
        #most common = 0
        else:
            epsilon += 1 << k-i

    return gamma * epsilon

def life_support(list_bits):
    """
    Iterate through a list of binary lines.
    Oxygen rating computation:
    Check for each position i, which bit is the most common.
    Then, only keep the lines with the most common bit at pos i.
    Continue until there is only one binary line.
    CO2 rating:
    Same, but with least common bit at each position.
    """

    count    = 0
    o2_bits  = [bits for bits in list_bits]
    co2_bits = [bits for bits in list_bits]
    o2  = 0
    co2 = 0
    i  = 0
    n1 = len(o2_bits)
    n2 = len(co2_bits)
    n  = len(list_bits[0]) - 1

    while n1 > 1 or n2 > 1:
        count_o2  = sum([bit[i] for bit in o2_bits])
        count_co2 = sum([bit[i] for bit in co2_bits])

        if n1 == 1:
            pass
        #in case of equality, choose 1 for the most common
        elif count_o2 >= n1/2:
            #most common = 1 ; least common = 0
            o2  += 1 << n-i
            o2_bits  = [bits for bits in o2_bits if bits[i] == 1]
        else:
            #most common = 0 ; least common = 1
            o2_bits  = [bits for bits in o2_bits if bits[i] == 0]
            
        if n2 == 1:
            pass
        #in case of equality, choose 0 for the least common
        elif count_co2 < n2/2:
            co2  += 1 << n-i
            co2_bits = [bits for bits in co2_bits if bits[i] == 1]
        else:
            co2_bits = [bits for bits in co2_bits if bits[i] == 0]
        #update values
        n1 = len(o2_bits)
        n2 = len(co2_bits)
        i += 1

    life_support_rating = o2 * co2

    return life_support_rating

def main():

    input_file = sys.argv[1]
    with open(input_file) as f:
        list_bits = f.read().splitlines()
        #convert str into list of int, once and for all
        list_bits = [[int(b) for b in bits] for bits in list_bits]
        power_consumption = gamma_epsilon(list_bits)
        life_support_rating = life_support(list_bits)

    print(f'This is the power_consumption: {power_consumption}')
    print(f'This is the life support rating: {life_support_rating}')
    return

if __name__ == '__main__':
    main()
