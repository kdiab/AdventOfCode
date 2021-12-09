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
        submarine_output.append(segment.split())

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
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[2] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 2:
                code_dict[3] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[5] = code
        #
        # cdfbe 5
        # cfe
        # cd
        # cdfe
        #
        # gcdfa 2
        # gcf
        # gcd
        # gcdf
        #
        # fbcad 3
        # fc
        # cd
        # fcd
        if len(code) == 6:
            # Possible Combinations: 9, 6, 0
            #
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 2 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[9] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 5 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 4:
                code_dict[6] = code
            if len(code.translate({ord(i): None for i in str(code_dict[1])})) == 4 and len(code.translate({ord(i): None for i in str(code_dict[4])})) == 3 and len(code.translate({ord(i): None for i in str(code_dict[7])})) == 3:
                code_dict[0] = code
            # cefabd = 9
            # cefd
            # cd
            # cef
            #
            # cdfgeb = 6
            # cdfge
            # cdg
            # cfge
            #
            # cagedb = 0
            # cged
            # cgd
            # cge

    out = sub_output[n].split()
    for o in out:
        for k in code_dict:
            if Counter(o) == Counter(code_dict[k]):
                total_output += str(k)

    print(total_output)
    print(code_dict)
    return total_output


sum_total_output = 0
for s in range(len(sub_input)):
    sum_total_output += int(fetch(s))
print(sum_total_output)
