# part 1
counter = 0
with open('input.txt') as f:
    input_content = [int(x) for x in f.read().split()]
    for i, number in enumerate(input_content):
        if i < (len(input_content) - 1):
            if number < input_content[i+1]:
                counter = counter + 1
print(f"part 1: {counter}")

# part 2
counter = 0
with open('input.txt') as f:
    input_content = [int(x) for x in f.read().split()]
    for i, number in enumerate(input_content):
        if i < (len(input_content) - 3):
            three_time_sum = number + input_content[i+1] + input_content[i+2]
            next_three_time_sum = input_content[i+1] + input_content[i+2] + input_content[i+3]
            if three_time_sum < next_three_time_sum:
                counter = counter + 1
print(f"part 2: {counter}")
