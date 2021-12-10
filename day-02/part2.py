# Solution to https://adventofcode.com/2021/day/2
# Input from https://adventofcode.com/2021/day/2/input

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
content = content.split('\n')

# Initialise values
aim = 0
depth = 0
horizontal = 0

for value in content:
    # Skip blank values
    if value != '':
        # Separate values into a command and a number
        command = value.split(' ')
        # Change appropriate value
        if command[0] == 'forward':
            horizontal += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])

# Multiply values for result
result = depth * horizontal

print(result)
