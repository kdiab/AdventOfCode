import numpy as np
import pandas as pd
# Part 1
with open('input.txt') as f:
    data = f.read().split(',')
crab_location = list(map(int, data))
# crab_location = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
# select a position
# for each value find the distance to that position
# add the distance to fuel counter
fuel_used = 0
crab_mean = int(np.median(crab_location))

for x, loc in enumerate(crab_location):
    if loc > crab_mean:
        fuel_used += loc - crab_mean
    else:
        fuel_used += crab_mean - loc

print(f"Fuel used in part 1: {fuel_used}")


# Part 2

with open('input.txt') as f:
    data = f.read().split(',')
crab_location = list(map(int, data))
# crab_location = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
# select a position
# for each value find the distance to that position
# add the sum of integers to fuel counter
# Sum of integers = n(n + 1)/2
fuel_used = 0
diff = 0
fastest_fuel = 99999999999999
#
for x in range(max(crab_location)): # for every possible location in range
    fuel_used = 0
    for crab in crab_location:
        if crab > x:
            diff = crab - x
            fuel_used += sum(range(diff+1))
        else:
            diff = x - crab
            fuel_used += sum(range(diff+1))
    if fuel_used < fastest_fuel:
        fastest_fuel = fuel_used
print(f"Fuel used in part 1: {fastest_fuel}")
