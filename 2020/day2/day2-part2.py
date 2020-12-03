import re

def getData():
    data = []
    with open('input.txt', 'r') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip('\r\n'))
        data = lines
    return(data)

data = getData()

num_passed = num_failed = 0
for line in data:
    pattern = re.compile("(\d+)-(\d+)\s([a-z]): (.*)")

    match = pattern.match(line)
    minimum = int(match.group(1))
    maximum = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    indexOneMatches = (password[minimum-1] == letter)
    indexTwoMatches = (password[maximum-1] == letter)
    passed = indexOneMatches ^ indexTwoMatches

    if passed:
        num_passed += 1
    else:
        num_failed += 1

print("Passed: {}".format(num_passed))
print("Failed: {}".format(num_failed))
