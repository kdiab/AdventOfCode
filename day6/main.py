import numpy as np
import pandas as pd

with open('input.txt') as f:
    data = f.read().split(',')
lantern_fish_population = list(map(int, data))
# part 1    n^2 solution
breeding_days = 256

for n in range(80):
    for i, fish in enumerate(lantern_fish_population):
        lantern_fish_population[i] -= 1
        if lantern_fish_population[i] == -1:
            lantern_fish_population[i] = 6
            lantern_fish_population.append(9)

# part 2 n^2 method taking forever so rethinking solution
# solution_1: dict with key as AGE of fish, total fish as value

# Layout:
#         AGE:NUMBER OF FISH
#         0: X
#         1: X
#         2: X
#         3: X
#         4: X
#         5: X
#         6: X
#         7: X
#         8: X
#   Idea: shift values up every day, so 8 -> 7. when fish hits -1, move back into 6,
#   add the amount in 6 to 8, and the amount in 7 to 6

lantern_fish_keys = np.arange(0, 9)
lantern_fish_dictionary = {}

# Initialize dictionary with keys 0 - 8 with input values
for lk in lantern_fish_keys:
    lantern_fish_dictionary[lk] = lantern_fish_population.count(lk)
#   {0: 0, 1: 207, 2: 30, 3: 22, 4: 19, 5: 22, 6: 0, 7: 0, 8: 0}
for day in range(breeding_days):
    new_fish = lantern_fish_dictionary[0]
    for k in lantern_fish_keys:
        #   shift values up if key is less than 8
        if k < 8:
            lantern_fish_dictionary[k] = lantern_fish_dictionary[k + 1]
    lantern_fish_dictionary[8] = new_fish
    lantern_fish_dictionary[6] += new_fish

total_fish = sum(lantern_fish_dictionary.values())
print(total_fish)
# shift values up
