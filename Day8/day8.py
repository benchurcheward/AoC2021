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

    #puzzle2
    #dico = {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'', 'g':''}
    #digits = ['']*10
    #for i in range(10):
    #    dico[i] = []
    with open(input_file) as f:
        sum_output = 0
        while(line := next(f, None)) is not None:
            unknown = []
            digits = [set() for i in range(10)]
            #print(line)
            line = line.split(' | ')
            signal = line[0].split(' ')
            output = line[1].strip().split(' ')
            #print(signal)
            #print('###############')
            #print(output)
            for word in signal:
                #print(word)
                word = set([l for l in word])
                #print(word)
                if len(word) == 2:
                    digits[1] = word
                    #print('1 found !')
                elif len(word) == 3:
                    digits[7] = word
                    #print('7 found !')
                elif len(word) == 4:
                    digits[4] = word
                    #print('4 found !')
                elif len(word) == 5:
                    unknown.append(word)
                elif len(word) == 6:
                    unknown.append(word)
                elif len(word) == 7:
                    digits[8] = word
                    #print('8 found !')
            while True:
                unknown = [word for word in unknown if word not in digits]
                #print(unknown)
                if not unknown:
                    #print('Terminated !')
                    break
                for word in unknown:
                    if len(word) == 5:
                        if digits[1].issubset(word):
                            #print('3 found !')
                            digits[3] = word
                        else:
                            if digits[6]:
                                #print(digits[6])
                                if len(word & digits[1] & digits[6]) == 1:
                                        digits[5] = word
                                        #print('5 found !')
                                        continue
                                else:
                                    digits[2] = word
                                    #print('2 found !')
                                    continue
                            else:
                                continue
                    if len(word) == 6:
                        if digits[4] <= word:
                            digits[9] = word
                            #print('9 found !')
                            continue
                        elif digits[7] <= word:
                            digits[0] = word
                            #print('0 found !')
                            continue
                        else:
                            digits[6] = word
                            #print(digits[6])
                            #print('6 found !')
                            continue
            #digits = [''.join(list(word)) for word in digits]
            #print(digits)
            #sum_output = 0
            number = ''
            #print(output)
            output = [set([l for l in word]) for word in output]
            for word in output:
                if word in digits:
                    number = f"{number}{digits.index(word)}"
            print(f"Number is {number}")
            sum_output += int(number)
            print(f"Sum of numbers are : {sum_output}")

if __name__ == '__main__':
    main()
