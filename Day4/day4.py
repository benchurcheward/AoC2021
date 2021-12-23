#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import numpy as np

def main():
    input_file = sys.argv[1]
    with open(input_file) as f:
        numbers = [int(n) for n in next(f).split(',')]
        bingos = []
        #construct bingo grids
        bingo_temp = []
        count = 0
        line_to_sum = []
        next(f)
        while(line := next(f, None)) is not None:
            temp = re.findall(r'\d+', line)
            #assert(temp)
            if not temp:
                bingos.append(np.array(bingo_temp))
                #bingos.append(np.array(bingo_temp))
                bingo_temp = []
                continue

            bingo_temp.append(list(map(int, temp)))
        bingos.append(np.array(bingo_temp))
        #bingos.append(np.array(bingo_temp))
        list_success = []
        set_success = set()
        rank = 0
        k = 0
        check_bingo = False
        while check_bingo == False:
            n = numbers[k]
            count += 1
            for b in range(len(bingos)):
                if b in set_success:
                    continue
                bingos[b] = np.where(bingos[b] == n, 0, bingos[b])
                if count >= 5:
                    for i in range(5):
                        row_zeros = np.count_nonzero(bingos[b][i,:])
                        col_zeros = np.count_nonzero(bingos[b][:,i])
                        if not row_zeros or not col_zeros:
                            sum_rest = np.sum(bingos[b])
                            list_success.append((b, n*sum_rest))
                            set_success.add(b)
                            if len(list_success) == len(bingos):
                                check_bingo = True
                            break
                if check_bingo == True:
                    break
            k += 1
        print(f"Answer from first completed grid: {list_success[0][1]}")
        print(f"Answer from last completed grid: {list_success[len(list_success)-1][1]}")

if __name__ == '__main__':
    main()
