# part 1

with open('input.txt') as f:
    input_content = f.read().split()
    # enumerate list
    forward = 0
    depth = 0
    for i, command in enumerate(input_content):
        # if command is encountered add int() of next line
        if "forward" in command:
            forward = forward + int(input_content[i+1])
        elif "up" in command:
            depth = depth - int(input_content[i+1])
        elif "down" in command:
            depth = depth + int(input_content[i + 1])

    print(f"Part 1: {forward * depth}")

# part 2

with open('input.txt') as f:
    input_content = f.read().split()
    # enumerate list
    forward = 0
    depth = 0
    aim = 0
    for i, command in enumerate(input_content):
        # if command is encountered add int() of next line
        if "forward" in command:
            forward = forward + int(input_content[i+1])
            depth = depth + (aim * int(input_content[i+1]))
        elif "up" in command:
            aim = aim - int(input_content[i + 1])
        elif "down" in command:
            aim = aim + int(input_content[i + 1])

    print(f"Part 2: {forward * depth}")
