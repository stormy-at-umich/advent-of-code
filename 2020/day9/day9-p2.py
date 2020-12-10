import re
import sys

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def isSumOfTwoIn(target,numberSet):
    isSum = False
    for number in numberSet:
        firstNumber = int(number)
        secondNumber = int(target) - firstNumber
        if str(secondNumber) in numberSet:
            isSum = True
            break
    return isSum

def contiguousAddends(target,numberSet):
    found = False
    currentIdx = 0
    contiguousSet = []
    for start in range(currentIdx,len(numberSet)):
        currentTally = 0
        for addendIdx in range(start,len(numberSet)):
            thisNumber = int(numberSet[addendIdx])
            currentTally += thisNumber
            contiguousSet.append(thisNumber)
            if currentTally == int(target):
                found = True
                break
            if currentTally > int(target):
                break
        if found:
            break 
        else:
            contiguousSet = []
    return(contiguousSet)

bufferSize = 25
currentIdx = bufferSize
currentBuffer = data[(currentIdx-bufferSize):currentIdx]
errorDetected = False
for lineNo in range(currentIdx,len(data)):
    line = data[lineNo]
    currentBuffer = data[(currentIdx-bufferSize):currentIdx]
    if not isSumOfTwoIn(data[currentIdx],currentBuffer):
        errorDetected = True
        break
    currentIdx += 1

if errorDetected:
    print(f"The number that doesn't add up is {data[currentIdx]}")
    ca = contiguousAddends(data[currentIdx],data)
    print(f"Contiguous addends are: {ca}")
    minPlusMax = min(ca) + max(ca)
    print(f"Min plus max is {minPlusMax}")
else:
    print("Nothing amiss")
