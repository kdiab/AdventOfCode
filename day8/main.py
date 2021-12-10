import itertools
from collections import Counter

# Part 1
with open('input.txt') as f:
    data = f.read()

data = list(map(lambda x: x.replace('|', ',').split(','), data.split('\n')))
# flatten array
data = list(itertools.chain(*data))

submarine_output = []
# Get only the 4 segment output
for i, segment in enumerate(data, start=1):
    if i % 2 == 0:
        # Input is presented as Input array, Output array
        # Get every other array which will be every Output array
        submarine_output.append(segment.split())
# Return 1 iterable basically flattening array of output after split
submarine_output = list(itertools.chain(*submarine_output))

count = 0
for s in submarine_output:
    if len(s) == 7 or len(s) == 2 or len(s) == 3 or len(s) == 4:
        count += 1
print(f"Number of occurrences: {count}")

# Part 2

with open('input.txt') as f:
    data = f.read()

data = list(map(lambda x: x.replace(' | ', ',').split(','), data.split('\n')))
# flatten array
data = list(itertools.chain(*data))

sub_input = []
sub_output = []
# Split input and output
for i, segment in enumerate(data, start=1):
    if i % 2 == 0:
        sub_output.append(segment.split(','))
    else:
        sub_input.append(segment.split(','))

# Flatten input and output
sub_input = list(itertools.chain(*sub_input))
sub_output = list(itertools.chain(*sub_output))
# Fetch method


def fetch(n):
    total_output = ''
    code_dict = {}
    codes = sub_input[n].split()
    # Find unique values 1 7 4 8 and add to dict
    for code in codes:
        if len(code) == 2:
            code_dict[1] = code
        if len(code) == 3:
            code_dict[7] = code
        if len(code) == 4:
            code_dict[4] = code
        if len(code) == 7:
            code_dict[8] = code
        # Find combinations of uniques and add to dict
    for code in codes:
        if len(code) == 5:
            # For segments of length 5
            # Subtract known numbers 1, 4, and 7 from the number
            # If the unique combination is met assign segment to dict
            # example:
            # cdfbe 5
            # cfe 5 - 1 = len 3
            # cd 5 - 4 = len 2
            # cdfe 5 - 7 = len 4
            #
            # Only the number 5 can have the output = to 3, 2, 4
            #
            # gcdfa 2
            # gcf 2 - 1 = 3
            # gcd 2 - 4 = 3
            # gcdf 2 - 7 = 4
            #
            # Only 2 can have the combination 3, 3, 4
            #
            # fbcad 3
            # fc 3 - 1 = 2
            # cd 3 - 4 = 2
            # fcd 3 - 7 = 3
            #
            # Only 3 can have the combination 2, 2, 3

            # len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4
            # This line gets the length of subtracting the strings from each other and comparing to 4
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[2] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 2:
                code_dict[3] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[5] = code
        if len(code) == 6:
            # Possible Combinations: 9, 6, 0
            #
            # cefabd = 9
            # cefd 9 - 1 = 4
            # cd 9 - 4 = 2
            # cef 9 - 7 = 3
            #
            # cdfgeb = 6
            # cdfge 6 - 1 = 5
            # cdg 6 - 4 = 3
            # cfge 6 - 7 = 4
            #
            # cagedb = 0
            # cged 0 - 1 = 4
            # cgd 0 - 4 = 3
            # cge 0 - 7 = 3
            #
            # Same logic as above but for segments of length 6
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[9] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 5 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 4:
                code_dict[6] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[0] = code
    out = sub_output[n].split()
    # Loop through the output
    for o in out:
        for k in code_dict:
            # Compare if the contents of output are equal to anything in dict
            if Counter(o) == Counter(code_dict[k]):
                total_output += str(k)
    return total_output


sum_total_output = 0
for s in range(len(sub_input)):
    sum_total_output += int(fetch(s))
print(f"Sum of decoded codes: {sum_total_output}")
