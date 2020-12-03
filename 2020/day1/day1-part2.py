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
        for lineThreeNo in range(lineTwoNo, numLines):
            thirdNo = data[lineThreeNo]
            if (firstNo + secondNo + thirdNo == 2020):
                print("The numbers are " + str(firstNo) + ", " + str(secondNo) + ", and " + str(thirdNo))
                print("Multiplied together, they are: " + str(firstNo * secondNo * thirdNo))
                sys.exit(0)

