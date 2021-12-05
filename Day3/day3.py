#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def gamma_epsilon(list_bits):
    """
    Iterate through a list of lines of bits.
    Computes gamma rate and epsilon rate, encoding as lines of bits:
    Bits of gamma are the most common bits at each position.
    Bits of espilon are the least common bits at each position.

    Returns product of gamma and epsilon.
    O(Nk+2k), with:
    N = number of binary lines in list_bits
    k = number of bits in one binary line
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
            counts[i] += binary[i]

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

    n = len(list_bits)
    count      = 0
    o2_bits  = [bits for bits in list_bits]
    co2_bits = [bits for bits in list_bits]
    o2_rating  = 0
    co2_rating = 0
    i = 0

    #I followed linearly the text of the exercise, but note that a single loop
    #is possible, saving time

    #compute o2_binary
    while n > 1:
        count = 0
        for binary in o2_bits:
            count += binary[i]
        #in case of equality, choose 1 for the most common,
        #0 for the last common
        if count >= n/2:
            most_common = 1
        else:
            most_common = 0

        #(re)construct the o2_bits list
        #keeping only the bits with the most common i-th bit
        o2_bits = [bits for bits in o2_bits if bits[i] == most_common]
        #update values
        n = len(o2_bits)
        i += 1

    #re-initiate n as original number of binary lines
    n = len(list_bits)
    i = 0

    #compute co2_binary
    while n > 1:
        count = 0
        for binary in co2_bits:
            count += binary[i]
        #in case of equalities, choose 0
        if count >= n/2:
            least_common = 0
        else:
            least_common = 1

        #(re)construct the co2_bits list
        #keeping only the bits with the least common i-th bit
        co2_bits = [bits for bits in co2_bits if bits[i] == least_common]
        #update values
        n = len(co2_bits)
        i += 1

    o2_bits  = o2_bits[0]
    co2_bits = co2_bits[0]
    n = len(o2_bits)

    #convert into decimals
    for i in range(n):
        if o2_bits[n-i-1] == 1:
            o2_rating += 2**i
        if co2_bits[n-i-1] == 1:
            co2_rating += 2**i

    ##note that the lines beyond do exactly the same thing
    ##using python list comprehension
    ##int(str, n) convert str to int following a base n
    #o2_rating = int(''.join([str(bit) for bit in o2_bits]), 2)
    #co2_rating = int(''.join([str(bit) for bit in co2_bits]), 2)

    life_support_rating = o2_rating * co2_rating

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
