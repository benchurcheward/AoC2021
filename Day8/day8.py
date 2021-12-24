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

    with open(input_file) as f:
        sum_output = 0
        while(line := next(f, None)) is not None:
            unknown = []
            digits = [set() for i in range(10)]
            line = line.split(' | ')
            signal = line[0].split(' ')
            output = line[1].strip().split(' ')

            for word in signal:
                word = set([l for l in word])
                if len(word) == 2:
                    digits[1] = word
                elif len(word) == 3:
                    digits[7] = word
                elif len(word) == 4:
                    digits[4] = word
                elif len(word) == 5:
                    unknown.append(word)
                elif len(word) == 6:
                    unknown.append(word)
                elif len(word) == 7:
                    digits[8] = word
            while True:
                unknown = [word for word in unknown if word not in digits]
                if not unknown:
                    break
                for word in unknown:
                    if len(word) == 5:
                        if digits[1] <= (word):
                            digits[3] = word
                        else:
                            if digits[6]:
                                if len(word & digits[1] & digits[6]) == 1:
                                        digits[5] = word
                                        continue
                                else:
                                    digits[2] = word
                                    continue
                            else:
                                continue
                    if len(word) == 6:
                        if digits[4] <= word:
                            digits[9] = word
                            continue
                        elif digits[7] <= word:
                            digits[0] = word
                            continue
                        else:
                            digits[6] = word
                            continue
            number = ''
            output = [set([l for l in word]) for word in output]
            for word in output:
                if word in digits:
                    number = f"{number}{digits.index(word)}"
            print(f"Number is {number}")
            sum_output += int(number)
        print(f"Sum of numbers are : {sum_output}")

if __name__ == '__main__':
    main()
