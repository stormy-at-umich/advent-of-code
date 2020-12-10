import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

instructions = []
for line in data:
    instruction, value = line.split(" ")
    instructions.append((instruction,value.replace("+","")))

complete = False
currentLineNumber = 0
tally = 0
seenLines = []
while not complete:
    instruction, value = instructions[currentLineNumber] 
    newLineNumber = currentLineNumber
    if instruction == "acc":
        tally += int(value)
        newLineNumber += 1
    elif instruction == "jmp":
        newLineNumber += int(value)
    else:
        newLineNumber += 1
    
    if newLineNumber in seenLines or newLineNumber > len(instructions):
        complete = True
    else:
        seenLines.append(currentLineNumber)

    currentLineNumber = newLineNumber

print(f"Tally is {tally}")
