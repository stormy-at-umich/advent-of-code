
with open("input.txt", "r") as f:
    data = f.read().splitlines()

countSum = 0
answerDict = {}
for row in data:
    if row != "":
        for letter in row:
            try:
                answerDict[letter] += 1
            except(KeyError):
                answerDict[letter] = 1
    else:
        """ new group """
        countSum += len(answerDict.keys())
        answerDict = {}
        continue

# catch the straggler
countSum += len(answerDict.keys())

print(f"Sum is {countSum}")
