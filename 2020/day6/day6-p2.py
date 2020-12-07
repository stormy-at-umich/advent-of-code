
with open("input.txt", "r") as f:
    data = f.read().splitlines()

def commonAnswerCount(answerDict,groupSize):
    numberAllAnswered = 0
    for letter in answerDict:
        if (answerDict[letter] == groupSize):
            numberAllAnswered += 1
    return(numberAllAnswered)

countSum = 0
answerDict = {}
groupSize = 0
for row in data:
    if row != "":
        groupSize += 1
        for letter in row:
            try:
                answerDict[letter] += 1
            except(KeyError):
                answerDict[letter] = 1
    else:
        """ new group """
        countSum += commonAnswerCount(answerDict,groupSize)
        groupSize = 0
        answerDict = {}
        continue

# catch the straggler
countSum += commonAnswerCount(answerDict,groupSize)

print(f"Sum is {countSum}")
