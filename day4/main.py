# Part 1
# VERY BAD SOLUTION

import numpy as np

# sample board input
# [['57' '80' '91' '40' '12']
#  ['62' '36' '72' '0' '20']
#  ['55' '60' '25' '92' '96']
#  ['14' '2' '17' '18' '86']
#  ['1' '4' '90' '66' '38']]

# input: [40, 0, 92, 18, 66] <- vertical bingo, 5 steps
# input: [55, 60, 25, 92, 96] <- horizontal bingo, 5 steps

from numpy import *

with open('bingoboards.txt') as f:
    matrix = f.read().split()
    # create matrix array for each bingo board
matrix = array(matrix).astype(int).reshape(-1, 5, 5)

with open('input.txt') as fi:
    bingo_input = fi.read().split(',')
m = matrix.copy()

# solve each bingo board individually and count how long it takes
# for each array
#   solve the bingo board
#         replace match with -1
for b, k in enumerate(bingo_input):
    count = 0
    for i, arr in enumerate(m):
        if i > 5:
            #         after the first 5 inputs, start checking if the board is solved
            #         Check if any boards are solved
            #           input > 5
            #           if row sum has -5, stop
            #           print the array and number of i
            # sum of each row and column
            row_sum = sum(m[i], axis=1, dtype=int)
            column_sum = sum(m[i], axis=0, dtype=int)
            for p in row_sum:
                for o in column_sum:
                    if o == -5:
                        print(f"Bingo board number: {i}")
                        print(f"\nBingo board: \n{matrix[i]}")
                        print(f"\nSolved Bingo board: \n{m[i]}")
                        print(f"\nLast number called: {bingo_input[b - 1]}")
                        array_sum = m[i].flatten()
                        bingo_number = 0
                        for a in array_sum:
                            if a == -1:
                                bingo_number += 1
                        print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
                        exit()
                    if p == -5:
                        print(f"Bingo board number: {i}")
                        print(f"\nBingo board: \n{matrix[i]}")
                        print(f"\nSolved Bingo board: \n{m[i]}")
                        print(f"\nLast number called: {bingo_input[b - 1]}")
                        array_sum = m[i].flatten()
                        bingo_number = 0
                        for a in array_sum:
                            if a == -1:
                                bingo_number += 1
                        print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
                        exit()
                        # exit after finding shortest bingo board
        for j, row in enumerate(arr):
            for z, element in enumerate(row):
                if m[i, j, z] == int(k):
                    m[i, j, z] = -1

# Part 2
