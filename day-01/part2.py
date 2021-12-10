# Solution to https://adventofcode.com/2021/day/1
# Input from https://adventofcode.com/2021/day/1/input

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
content = content.split('\n')

previous = None
counter = 0

# Loop to length-3 because we need groups of three numbers, so anything past the third to last number isn't usable
# and the text file has a blank line at the end of it which counts as a separate value
for i in range(0, len(content)-3):
    value = int(content[i]) + int(content[i+1]) + int(content[i+2])
    if i > 0:
        if value > previous:
            counter += 1

    previous = value

print(counter)
