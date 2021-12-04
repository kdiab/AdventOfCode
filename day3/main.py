# part 1

with open('input.txt') as f:
    input_content = f.read().split()
    # enumerate list
    majority_one = 0
    majority_zero = 0
    binary_string = ""
    inverse_binary_string = ""
    for n in range(12):
        for i, command in enumerate(input_content):
            if int(input_content[i][n]) == 1:
                majority_one = majority_one + 1
            elif int(input_content[i][n]) == 0:
                majority_zero = majority_zero + 1
        if majority_one > majority_zero:
            binary_string = binary_string + '1'
        else:
            binary_string = binary_string + '0'
        majority_zero = 0
        majority_one = 0
    print(int(binary_string, 2))
    #inverse bit string
    for bit in binary_string:
        if bit == "1":
            inverse_binary_string += "0"
        else:
            inverse_binary_string += "1"
    print(int(inverse_binary_string, 2))

    print(f" Part 1: {int(inverse_binary_string, 2) * int(binary_string, 2)}")

# part 2


def oxygen_input(n):
    with open('input.txt') as f:
        oxygen_content = f.read().split()
    # enumerate list

    for k in range(n):
        majority_one = []
        majority_zero = []
        for i, line in enumerate(oxygen_content):
            if int(oxygen_content[i][k]) == 1:
                majority_one.append(line)
            elif int(oxygen_content[i][k]) == 0:
                majority_zero.append(line)
        if len(majority_one) > len(majority_zero):
            oxygen_content = majority_one
        elif len(majority_one) < len(majority_zero):
            oxygen_content = majority_zero
        elif len(majority_one) == len(majority_zero):
            oxygen_content = majority_one
    print(oxygen_content)
    return oxygen_content[0]


def carbon_input(n):
    with open('input.txt') as f:
        carbon_content = f.read().split()
    # enumerate list

    for k in range(n):
        majority_one = []
        majority_zero = []
        for i, line in enumerate(carbon_content):
            if int(carbon_content[i][k]) == 1:
                majority_one.append(line)
            elif int(carbon_content[i][k]) == 0:
                majority_zero.append(line)
        if len(majority_one) < len(majority_zero):
            carbon_content = majority_one
        elif len(majority_one) > len(majority_zero):
            carbon_content = majority_zero
        elif len(majority_one) == len(majority_zero):
            carbon_content = majority_zero
        if len(carbon_content) == 1:
            print(carbon_content)
            return carbon_content[0]


oxygen = oxygen_input(12)
carbon = carbon_input(12)
print(f"Part 2: int(oxygen, 2) * int(carbon, 2)")

