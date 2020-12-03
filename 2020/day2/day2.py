import sys, re

def getData():
    data = []
    with open('input.txt', 'r') as file:
        lines = []
        for line in file:
            lines.append(line.rstrip('\r\n'))
        data = lines
    return(data)

data = getData()
num_passed = 0
num_failed = 0
for line in data:
    pattern = re.compile("(\d+)-(\d+)\s([a-zA-Z]): (.*)")
    match = pattern.match(line)
    minimum = int(match.group(1))
    maximum = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)

    replace = r"[^"+letter+"]"
    compressed_pass = re.sub(replace,'',password)
    number_letters = len(compressed_pass)
    if (number_letters > maximum or number_letters < minimum):
        num_failed += 1
    else:
        num_passed += 1

print("Passed: {}".format(num_passed))
print("Failed: {}".format(num_failed))
