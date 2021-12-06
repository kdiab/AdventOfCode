# Part 1
# VERY BAD SOLUTION

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
# for b, k in enumerate(bingo_input):
#     count = 0
#     for i, arr in enumerate(m):
#         if i > 5:
#             #         after the first 5 inputs, start checking if the board is solved
#             #         Check if any boards are solved
#             #           input > 5
#             #           if row sum has -5, stop
#             #           print the array and number of i
#             # sum of each row and column
#             row_sum = sum(m[i], axis=1, dtype=int)
#             column_sum = sum(m[i], axis=0, dtype=int)
#             for o in column_sum:
#                 if o == -5:
#                     print(f"Bingo board number: {i}")
#                     print(f"\nBingo board: \n{matrix[i]}")
#                     print(f"\nSolved Bingo board: \n{m[i]}")
#                     print(f"\nLast number called: {bingo_input[b - 1]}")
#                     array_sum = m[i].flatten()
#                     bingo_number = 0
#                     for a in array_sum:
#                         if a == -1:
#                             bingo_number += 1
#                     print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
#                     exit()
#             for p in row_sum:
#                 if p == -5:
#                     print(f"Bingo board number: {i}")
#                     print(f"\nBingo board: \n{matrix[i]}")
#                     print(f"\nSolved Bingo board: \n{m[i]}")
#                     print(f"\nLast number called: {bingo_input[b - 1]}")
#                     array_sum = m[i].flatten()
#                     bingo_number = 0
#                     for a in array_sum:
#                         if a == -1:
#                             bingo_number += 1
#                     print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
#                     exit()
#                     # exit after finding shortest bingo board
#         for j, row in enumerate(arr):
#             for z, element in enumerate(row):
#                 if m[i, j, z] == int(k):
#                     m[i, j, z] = -1

# Part 2


def solve_board(single_matrix):
    flag = False
    time_to_solve = 0
    champion_time = 0
    contending_time = 0
    contending_matrix = 0
    contending_row = 0
    contending_column = 0
    last_input = ''

    for binput in bingo_input:
        time_to_solve += 1
        for j, row in enumerate(single_matrix):
            for k, val in enumerate(row):
                if val == int(binput):
                    if flag is False:
                        single_matrix[j, k] = -1
                        row_sum = sum(single_matrix, axis=1, dtype=int)
                        column_sum = sum(single_matrix, axis=0, dtype=int)
                        if -5 in row_sum:
                            contending_time = time_to_solve
                            contending_matrix = single_matrix
                            contending_row = row_sum
                            contending_column = column_sum
                            last_input = binput
                            flag = True
                        elif -5 in column_sum:
                            contending_time = time_to_solve
                            contending_matrix = single_matrix
                            contending_row = row_sum
                            contending_column = column_sum
                            last_input = binput
                            flag = True
                    else:
                        if contending_time > champion_time:
                            champion_time = contending_time
                            champion_matrix = contending_matrix
                            champion_row = contending_row
                            champion_column = contending_column
                            print("-------------------------")
                            print(champion_matrix)
                            print(f"\nLast number called: {last_input}")
                            print(champion_row, champion_column, "\n")
                            print(f"Calls to solve: {champion_time}")
                            print("-------------------------")
                        else:
                            return


for i, arr in enumerate(m):
    solve_board(m[i])
    print((sum([76, 128,  -4,  87, -5]) + 16) * 10)

# manually search for longest matrix cause bad at code
# [[-1 -1  9 -1 70]
#  [41 -1 90 -1 -1]
#  [-1 -1  0 -1 -1]
#  [ 8 46 -1 29  5]
#  [-1 -1 -1 -1 -1]]
#
# Last number called: 9
# [ 76 128  -4  87  -5] [46 42 97 25 72]
#
# Calls to solve: 82

    # for o in column_sum:
    #     if o == -5:
    #         print(f"Bingo board number: {i}")
    #         print(f"\nBingo board: \n{matrix[i]}")
    #         print(f"\nSolved Bingo board: \n{m[i]}")
    #         print(f"\nLast number called: {bingo_input[b - 1]}")
    #         array_sum = m[i].flatten()
    #         bingo_number = 0
    #         for a in array_sum:
    #             if a == -1:
    #                 bingo_number += 1
    #         print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
    #         break
    # for p in row_sum:
    #     if p == -5:
    #         print(f"Bingo board number: {i}")
    #         print(f"\nBingo board: \n{matrix[i]}")
    #         print(f"\nSolved Bingo board: \n{m[i]}")
    #         print(f"\nLast number called: {bingo_input[b - 1]}")
    #         array_sum = m[i].flatten()
    #         bingo_number = 0
    #         for a in array_sum:
    #             if a == -1:
    #                 bingo_number += 1
    #         print((sum(array_sum) + bingo_number) * int(bingo_input[b - 1]))
    #         break

