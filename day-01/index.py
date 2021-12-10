# Solution to https://adventofcode.com/2021/day/1
# Input from https://adventofcode.com/2021/day/1/input

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
content = content.split('\n')

previous = None
counter = 0

# Loop through every value
for value in content:
    if value == '':
        break
    value = int(value)
    # If value > previous, increment counter
    # Else do nothing
    if previous != None:
        if value > previous:
            counter += 1
    previous = value

print(counter)
