import sys

data = []
with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        lines.append(int(line.rstrip('\r\n')))
    data = lines

target = 2020
numLines = len(data)
for lineNo in range(numLines):
    firstNo = data[lineNo]
    secondNo = 0
    for lineTwoNo in range(lineNo,numLines):
        secondNo = data[lineTwoNo]
        if (firstNo + secondNo == 2020):
            print("The numbers are " + str(firstNo) + " and " + str(secondNo))
            print("Multiplied together, they are: " + str(firstNo * secondNo))
            sys.exit(0)

