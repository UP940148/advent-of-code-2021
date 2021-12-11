# Solution to https://adventofcode.com/2021/day/4
# Input from https://adventofcode.com/2021/day/4/input

# Import system to stop code later
import sys

# Create board class
class Board:
    def __init__(self, asString):
        self.rows = asString.split('\n')
        for i in range(0, len(self.rows)):
            self.rows[i] = self.rows[i].split(' ')
            # If any blank elements in row, remove
            while self.rows[i].count('') > 0:
                self.rows[i].remove('')

    def checkIfComplete(self, values):

        # Loop through rows
        for i in range(0, 5):
            # Reset counter
            counter = 0
            # Loop through columns
            for j in range(0, 5):
                # If current element in called out values, increment counter
                if values.count(self.rows[i][j]) > 0:
                    counter += 1
            # If row has 5 matches, then this board wins
            if counter == 5:
                return True, self.getUnmarkedSum(values)

        # Loop through columns
        for i in range(0, 5):
            # Reset counter
            counter = 0
            # Loop through rows
            for j in range(0, 5):
                # If current element in called out values, increment counter
                if values.count(self.rows[j][i]) > 0:
                    counter += 1
            # If column has 5 matches, then this board wins
            if counter == 5:
                return True, self.getUnmarkedSum(values)

        # If no rows or columns complete, return false
        return False, -1

    def getUnmarkedSum(self, values):
        unmarked = []
        for i in range(0, 5):
            for j in range(0, 5):
                # If value not called out, add to unmarked
                if values.count(self.rows[i][j]) == 0:
                    unmarked.append(self.rows[i][j])
        # Add up all unmarked values
        total = 0
        for element in unmarked:
            total += int(element)

        return total




# Open file and read contents
file = open('./input.txt', 'r')

callouts = file.readline() # Get line of called out numbers
callouts = callouts.strip() # Remove line break at end of line
callouts = callouts.split(',') # Convert to list

content = file.read()
# Split into individual boards
boards = content.split('\n\n')

# Create and track board objects
boardList = []
for board in boards:
    boardList.append(Board(board.strip())) # Create new board from data, after stripping leading and trailing new lines

# Loop through every called out number
called = []
while len(callouts) > 0:
    called.append(callouts.pop(0)) # Remove first element from callouts and add to called
    for board in boardList:
        complete, value = board.checkIfComplete(called)
        if complete:
            total = value * int(called[-1])
            print(total)
            sys.exit()
