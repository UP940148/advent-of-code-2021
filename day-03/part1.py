# Solution to https://adventofcode.com/2021/day/3
# Input from https://adventofcode.com/2021/day/3/input

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
content = content.split('\n')

# Initialise values
gammaRate = ''
epsilonRate = ''

# Loop every character in the binary strings
for j in range(0, len(content[0])):
    # Reset counters to zero
    zeroCount = 0
    oneCount = 0
    # Loop through every string
    for i in range(0, len(content)-1):
        # Increment counter based on subject character value
        if content[i][j] == '0':
            zeroCount += 1
        else:
            oneCount += 1

    # Create gamma and epsilon values for this position
    if zeroCount > oneCount:
        gammaRate += '0'
        epsilonRate += '1'
    else:
        gammaRate += '1'
        epsilonRate += '0'

# Multiply and return
result = int(epsilonRate, 2) * int(gammaRate, 2)
print(result)
