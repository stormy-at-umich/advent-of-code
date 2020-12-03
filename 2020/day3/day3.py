import sys, re

def getData():
    data = []
    with open('input.txt', 'r') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip('\r\n'))
        data = lines
    return(data)

data = getData()

tree = '#'
row = col = treeCount = 0
numColumns = len(data[0])
for row in data:
    contents = row[col % numColumns]
    col += 3
    if contents == tree:
        treeCount += 1

print("You would hit {} trees".format(treeCount))
