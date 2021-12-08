import pandas as pd
import numpy as np

with open('input.txt') as f:
    data = f.read()
# Getting input
data = list(map(lambda x: x.replace('->', ',').split(','), data.split("\n")))
df = pd.DataFrame(data)
df = df.astype(int)
# Part 1
# zero_matrix = np.zeros([1000, 1000], dtype=int)
#
#
# def generate_data():
#     for i in range(len(df)):
#         # if x1 == x2
#         if df.loc[i, 0] == df.loc[i, 2]:
#             # if y1 - y2 is negative
#             if df.loc[i, 1] - df.loc[i, 3] < 0:
#                 # range = y2 - y1
#                 for y in range(df.loc[i, 3] - df.loc[i, 1]):
#                     y_coordinates = df.loc[i, 1] + y
#                     # loop through numbers between y2 and y1 and increment zero_matrix by 1
#                     zero_matrix[df.loc[i, 0], y_coordinates] += 1
#                 zero_matrix[df.loc[i, 0], df.loc[i, 3]] += 1
#
#             else:
#                 for y in range(df.loc[i, 1] - df.loc[i, 3]):
#                     y_coordinates = df.loc[i, 3] + y
#                     zero_matrix[df.loc[i, 0], y_coordinates] += 1
#                 zero_matrix[df.loc[i, 0], df.loc[i, 1]] += 1
#
#         elif df.loc[i, 1] == df.loc[i, 3]:
#             if df.loc[i, 0] - df.loc[i, 2] < 0:
#                 for x in range(df.loc[i, 2] - df.loc[i, 0]):
#                     x_coordinates = df.loc[i, 0] + x
#                     zero_matrix[x_coordinates, df.loc[i, 1]] += 1
#                 zero_matrix[df.loc[i, 2], df.loc[i, 1]] += 1
#
#             else:
#                 for x in range(df.loc[i, 0] - df.loc[i, 2]):
#                     x_coordinates = df.loc[i, 2] + x
#                     zero_matrix[x_coordinates, df.loc[i, 1]] += 1
#                 zero_matrix[df.loc[i, 0], df.loc[i, 1]] += 1
#
#
# generate_data()
# zero_matrix = pd.DataFrame(zero_matrix).transpose()
# count = (zero_matrix.values > 1).sum()
# print(zero_matrix, "\n\n\n", f"count = {count}")
# Sample Data:
#      0     1     2    3
# 0  565  190    756  381
# 1  402  695    402  138
# 2  271  844     98  844
# 3  276   41    276  282
# 4   12   93    512  593

# max in data in each column(df.max)
# 0     989
# 1     989
# 2     99
# 3     988
# Matrix needs to be 1000x1000

# Part 2
zero_matrix = np.zeros([1000, 1000], dtype=int)


def generate_data():
    for i in range(len(df)):
        # if x1 == x2
        if df.loc[i, 0] == df.loc[i, 2]:
            # if y1 - y2 is negative
            if df.loc[i, 1] - df.loc[i, 3] < 0:
                # range = y2 - y1
                for y in range(df.loc[i, 3] - df.loc[i, 1]):
                    y_coordinates = df.loc[i, 1] + y
                    # loop through numbers between y2 and y1 and increment zero_matrix by 1
                    zero_matrix[df.loc[i, 0], y_coordinates] += 1
                zero_matrix[df.loc[i, 0], df.loc[i, 3]] += 1

            else:
                for y in range(df.loc[i, 1] - df.loc[i, 3]):
                    y_coordinates = df.loc[i, 3] + y
                    zero_matrix[df.loc[i, 0], y_coordinates] += 1
                zero_matrix[df.loc[i, 0], df.loc[i, 1]] += 1

        elif df.loc[i, 1] == df.loc[i, 3]:
            if df.loc[i, 0] - df.loc[i, 2] < 0:
                for x in range(df.loc[i, 2] - df.loc[i, 0]):
                    x_coordinates = df.loc[i, 0] + x
                    zero_matrix[x_coordinates, df.loc[i, 1]] += 1
                zero_matrix[df.loc[i, 2], df.loc[i, 1]] += 1

            else:
                for x in range(df.loc[i, 0] - df.loc[i, 2]):
                    x_coordinates = df.loc[i, 2] + x
                    zero_matrix[x_coordinates, df.loc[i, 1]] += 1
                zero_matrix[df.loc[i, 0], df.loc[i, 1]] += 1

        #         IF x1 = y1 and x2 = y2
        elif df.loc[i, 0] == df.loc[i, 1] and df.loc[i, 2] == df.loc[i, 3]:
            # x1 - x2
            if df.loc[i, 0] - df.loc[i, 2] < 0:
                for d in range(df.loc[i, 2] - df.loc[i, 0]):
                    x_coordinate = df.loc[i, 0] + d
                    y_coordinate = df.loc[i, 1] + d
                    zero_matrix[x_coordinate, y_coordinate] += 1
                zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1
            else:
                for d in range(df.loc[i, 0] - df.loc[i, 2]):
                    x_coordinate = df.loc[i, 0] - d
                    y_coordinate = df.loc[i, 1] - d
                    zero_matrix[x_coordinate, y_coordinate] += 1
                zero_matrix[df.loc[i, 0], df.loc[i, 1]] += 1
        #         IF x1 = y2 and y1 = x2 e.g: 8,0 -> 0,8
        elif df.loc[i, 0] == df.loc[i, 3] and df.loc[i, 1] == df.loc[i, 2]:
            if df.loc[i, 0] > df.loc[i, 1]:
                for d in range(df.loc[i, 0] - df.loc[i, 1]):
                    x_coordinate = df.loc[i, 0] - d
                    y_coordinate = df.loc[i, 1] + d
                    zero_matrix[x_coordinate, y_coordinate] += 1
                zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1
            else:
                for d in range(df.loc[i, 1] - df.loc[i, 0]):
                    x_coordinate = df.loc[i, 0] + d
                    y_coordinate = df.loc[i, 1] - d
                    zero_matrix[x_coordinate, y_coordinate] += 1
                zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1
        else:
            if df.loc[i, 0] - df.loc[i, 2] == df.loc[i, 1] - df.loc[i, 3]:
                if df.loc[i, 0] - df.loc[i, 2] > 0:
                    for d in range(df.loc[i, 0] - df.loc[i, 2]):
                        x_coordinate = df.loc[i, 0] - d
                        y_coordinate = df.loc[i, 1] - d
                        zero_matrix[x_coordinate, y_coordinate] += 1
                    zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1
                # 6,4 -> 2,0
                else:
                    for d in range(df.loc[i, 2] - df.loc[i, 0]):
                        x_coordinate = df.loc[i, 0] + d
                        y_coordinate = df.loc[i, 1] + d
                        zero_matrix[x_coordinate, y_coordinate] += 1
                    zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1

            else:
                if df.loc[i, 0] - df.loc[i, 2] < 0:
                    for d in range(df.loc[i, 2] - df.loc[i, 0]):
                        x_coordinate = df.loc[i, 0] + d
                        y_coordinate = df.loc[i, 1] - d
                        zero_matrix[x_coordinate, y_coordinate] += 1
                    zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1
                else:
                    for d in range(df.loc[i, 0] - df.loc[i, 2]):
                        x_coordinate = df.loc[i, 0] - d
                        y_coordinate = df.loc[i, 1] + d
                        zero_matrix[x_coordinate, y_coordinate] += 1
                    zero_matrix[df.loc[i, 2], df.loc[i, 3]] += 1


generate_data()
zero_matrix = pd.DataFrame(zero_matrix).transpose()
count = (zero_matrix.values > 1).sum()
print(zero_matrix, "\n\n\n", f"count = {count}")
