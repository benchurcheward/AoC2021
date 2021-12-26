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

def main():
    input_file = sys.argv[1]

    with open(input_file) as f:
        lines = f.read().splitlines()

        corrupted = []
        opened = {'(', '[', '{', '<'}
        closed = {')', ']', '}', '>'}

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

    print(f"Sum of corrupted characters is {sum_corrupted(corrupted)}.")

if __name__ == '__main__':
    main()
