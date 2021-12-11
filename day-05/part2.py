# Solution to https://adventofcode.com/2021/day/5
# Input from https://adventofcode.com/2021/day/5/input

# Create Vent class
class Vent:
    def __init__(self, pos):
        self.p1 = pos[0].split(',')
        self.p2 = pos[1].split(',')
        self.p1[0] = int(self.p1[0])
        self.p1[1] = int(self.p1[1])
        self.p2[0] = int(self.p2[0])
        self.p2[1] = int(self.p2[1])
        self.plotSelf()

    def isStraight(self):
        # Vent is straight if either both x co-ordinates are the same or both y co-ordinates
        if self.p1[0] == self.p2[0] or self.p1[1] == self.p2[1]:
            return True
        return False

    def plotSelf(self):
        hits = []
        if self.isStraight():
            # If x is the same, then log all vertical points
            if self.p1[0] == self.p2[0]:
                values = [self.p1[1], self.p2[1]]
                values.sort()
                for i in range(values[0], values[1]+1):
                    newHit = str(self.p1[0]) + ',' + str(i)
                    hits.append(newHit)

            # If y is the same, then log all horizontal points
            elif self.p1[1] == self.p2[1]:
                values = [self.p1[0], self.p2[0]]
                values.sort()
                for i in range(values[0], values[1]+1):
                    newHit = str(i) + ',' + str(self.p1[1])
                    hits.append(newHit)
        else:
            # If diagonal
            if self.p1[0] < self.p2[0]:
                if self.p1[1] < self.p2[1]:
                    # SE ++
                    diff = self.p2[0] - self.p1[0]
                    for i in range(0, diff + 1):
                        newHit = str(self.p1[0] + i) + ',' + str(self.p1[1] + i)
                        hits.append(newHit)

                else:
                    # NE +-
                    diff = self.p2[0] - self.p1[0]
                    for i in range(0, diff + 1):
                        newHit = str(self.p1[0] + i) + ',' + str(self.p1[1] - i)
                        hits.append(newHit)
            else:
                if self.p1[1] < self.p2[1]:
                    # SW -+
                    diff = self.p1[0] - self.p2[0]
                    for i in range(0, diff + 1):
                        newHit = str(self.p1[0] - i) + ',' + str(self.p1[1] + i)
                        hits.append(newHit)
                else:
                    # NW --
                    diff = self.p1[0] - self.p2[0]
                    for i in range(0, diff + 1):
                        newHit = str(self.p1[0] - i) + ',' + str(self.p1[1] - i)
                        hits.append(newHit)


        # Log hits
        for point in hits:
            hitLog.append(point)
            # If point not hit before, then log as new unique point
            if uniqueLocations.count(point) == 0:
                uniqueLocations.append(point)

# Open file and read contents
file = open('./input.txt', 'r')
content = file.read()

# Split string into array of values
coords = content.split('\n')
# Remove blank line at the end
coords.pop()

hitLog = []
uniqueLocations = []

for i in range(0, len(coords)):
    coords[i] = coords[i].split(' -> ')
    Vent(coords[i])


count = 0
for pos in uniqueLocations:
    if hitLog.count(pos) > 1:
        count += 1

print(count)
