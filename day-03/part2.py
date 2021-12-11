# Solution to https://adventofcode.com/2021/day/3
# Input from https://adventofcode.com/2021/day/3/input

# Import regex
import re

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
content = content.split('\n')

# Initialise values
OGRating = ''
CO2Rating = ''
j = 0

# Until full length string made
while j < 12:
    # Reset counters
    zeroCount = 0
    oneCount = 0

    # Oxygen Generator Rating
    # For every string
    for i in range(0, len(content)-1):
        # If string matches regex (Previous characters match)
        matchString = "^" + OGRating + ".*"
        if not re.match(matchString, content[i]):
            continue
        subjectString = content[i]
        # Add up all ones and all zeros
        if subjectString[j] == '0':
            zeroCount += 1
        else:
            oneCount += 1

    # If only one value searched, it must be the answer
    if zeroCount + oneCount == 1:
        OGRating = subjectString
        break

    # If oneCount greater than zeroCount, then add a 1, else add a 0
    if oneCount >= zeroCount:
        OGRating += '1'
    else:
        OGRating += '0'

    j = len(OGRating)

# Reset j
j = 0

while j < 12:
    #print(matchString)
    zeroCount = 0
    oneCount = 0

    # CO2 Rating
    # For every string
    for i in range(0, len(content)-1):
        # If string matches regex (Previous characters match)
        matchString = "^" + CO2Rating + ".*"
        if not re.match(matchString, content[i]):
            continue
        subjectString = content[i]
        # Add up all ones and all zeros
        if subjectString[j] == '0':
            zeroCount += 1
        else:
            oneCount += 1

    # If only one value searched, it must be the answer
    #print(zeroCount, ' : ', oneCount)
    if zeroCount + oneCount == 1:
        #print('found : ', j)
        CO2Rating = subjectString
        break

    # If zeroCount less than oneCount, then add a 0, else add a 1
    if zeroCount <= oneCount:
        CO2Rating += '0'
    else:
        CO2Rating += '1'

    j = len(CO2Rating)


# Multiply and return result
result = int(OGRating, 2) * int(CO2Rating, 2)

print(result)
