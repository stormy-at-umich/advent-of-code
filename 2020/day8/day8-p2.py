import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

instructions = []
for line in data:
    instruction, value = line.split(" ")
    instructions.append((instruction,int(value.replace("+",""))))

changeableLines = []
rowNumber = 0
for instruction, value in instructions:
    if instruction == "jmp" or (instruction == "nop" and value != 0):
        changeableLines.append(rowNumber)
    rowNumber += 1

complete = False
for lineNumber in changeableLines:

    instrCopy = instructions.copy()
    
    toSwapInstr, toSwapValue = instrCopy[lineNumber]
    toSwapInstr = "nop" if toSwapInstr == "jmp" else "jmp"
    instrCopy[lineNumber] = (toSwapInstr, toSwapValue)

    currentLineNumber = tally = 0
    seenLines = []
    looping = False
    while not (looping or complete):
        instruction, value = instrCopy[currentLineNumber] 
        newLineNumber = currentLineNumber
        if instruction == "acc":
            tally += value
            newLineNumber += 1
        elif instruction == "jmp":
            newLineNumber += value
        else:
            newLineNumber += 1
        
        if newLineNumber in seenLines:
            looping = True
        else:
            seenLines.append(currentLineNumber)

        if newLineNumber > (len(instructions)-1):
            complete = True

        currentLineNumber = newLineNumber

    if complete:
        break

print(f"Tally from successful completion is {tally}")
