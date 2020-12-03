import sys

def getData():
    data = []
    with open('input.txt', 'r') as file:
        lines = []
        for line in file:
            lines.append(int(line.rstrip('\r\n')))
        data = lines
    return(data)

def sumTo(targetSum, targetDepth, currentDepth, operandSet, numberSet):

    qtyInSet = len(numberSet)

    for numberNumber in range(0,qtyInSet):

        thisNumber = numberSet[numberNumber]

        try:
            operandSet[currentDepth] = thisNumber 
        except(IndexError):
            operandSet.append(thisNumber)

        if (targetDepth == currentDepth):
            numSum = 0
            for number in operandSet:
                numSum += number
            if (numSum == targetSum):
                return(operandSet)
            else:
                """ does not add up """
        else:
            answer = sumTo(targetSum, targetDepth, currentDepth+1, operandSet, numberSet[1:])
            if (answer != False):
                return(answer)

    return(False)

def multiplyArray(arr):
    product = 1
    for e in arr:
        product *= e
    return product

target = 2020
depth = 3
data = getData()
finalNumberSet = sumTo(target, depth-1, 0, [], data)
print("Numbers are: " + (", ".join(map(str,finalNumberSet))))
print("Product is: {}".format(multiplyArray(finalNumberSet)))
