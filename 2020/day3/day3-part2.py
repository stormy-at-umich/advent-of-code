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
numColumns = len(data[0])

slopeAngles = [(1,1),(3,1),(5,1),(7,1),(1,2)]
slopeAngleNumber = 1
multiplesOfTreesHit = 1
for angle in slopeAngles:
    colNo = rowNo = 0
    shiftX = angle[0]
    shiftY = angle[1]
    treeCount = 0;
    for row in data:

        skipRow = (rowNo % shiftY) != 0
        rowNo += 1

        if skipRow:
            continue
            
        contents = row[colNo % numColumns]
        if contents == tree:
            treeCount += 1

        colNo += shiftX
    print("Trees hit for #{}: {}".format(slopeAngleNumber,treeCount))
    multiplesOfTreesHit *= treeCount
    slopeAngleNumber += 1

print("Answer to question is {}".format(multiplesOfTreesHit))
