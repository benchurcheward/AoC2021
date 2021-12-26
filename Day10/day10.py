#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

def is_valid(o, c):
    if o == '(':
        return c == ')'
    if o == '[':
        return c == ']'
    if o == '{':
        return c == '}'
    if o == '<':
        return c == '>'

def sum_corrupted(line):
    count = 0
    for l in line:
        if l == ')':
            count += 3
        if l == ']':
            count += 57
        if l == '}':
            count += 1197
        if l == '>':
            count += 25137
    return count

def complement(c):
    if c == '(':
        return ')'
    if c == '[':
        return ']'
    if c == '{':
        return '}'
    if c == '<':
        return '>'

def score_char(c):
    if c == '(':
        return 1
    if c == '[':
        return 2
    if c == '{':
        return 3
    if c == '<':
        return 4

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        lines = f.read().splitlines()

        corrupted = []
        opened = {'(', '[', '{', '<'}
        closed = {')', ']', '}', '>'}
        total_score = []
        for line in lines:
            opened_char = []
            line = [l for l in line][::-1]
            while line:
                l = line.pop()
                if l in opened:
                    opened_char.append(l)
                else:
                    if not opened_char:
                        corrupted.append(l)
                        break
                    if not is_valid(opened_char.pop(), l):
                        corrupted.append(l)
                        opened_char = []
                        break
            if opened_char:
                #print(opened_char)
                opened_char = opened_char[::-1]
                complement_char = [complement(c) for c in opened_char]
                print(''.join(complement_char))
                score = 0
                for c in opened_char:
                    score = score*5 + score_char(c)
                total_score.append(score)

    print(f"Sum of corrupted characters is {sum_corrupted(corrupted)}.")
    middle_score = int(len(total_score)/2)
    print(sorted(total_score)[middle_score])

if __name__ == '__main__':
    main()
