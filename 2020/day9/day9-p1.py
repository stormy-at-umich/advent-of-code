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
#    if isSum:
#        print(f"{target} is sum of two in {numberSet}")
#    else:
#        print(f"{target} is not sum of two in {numberSet}")
    return isSum

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
else:
    print("Nothing amiss")
