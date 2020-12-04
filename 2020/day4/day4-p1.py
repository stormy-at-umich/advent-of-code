
with open("input.txt", "r") as f:
    data = f.read().splitlines()

requiredFields = {
    "byr" : "Birth Year",
    "iyr" : "Issue Year",
    "eyr" : "Expiration Year",
    "hgt" : "Height",
    "hcl" : "Hair Color",
    "ecl" : "Eye Color",
    "pid" : "Passport ID",
    "cid" : "Country ID"
}

def parsePassportData(ppString):
    chunks = ppString.split(" ")
    passportDict = {}
    for chunk in chunks:
        (key,value) = chunk.split(":")
        passportDict[key] = value
    return(passportDict) 
    

passportData = []
thisPassport = ""
ppLineNo = 0
for row in data:
    if row == "":
        """ new passport """
        passportData.append(parsePassportData(thisPassport))
        thisPassport = ""
        ppLineNo = 0
        continue
    if ppLineNo > 0:
        thisPassport += " "
    thisPassport += row
    ppLineNo += 1
    
# One left at EOF to add, since no trailing newline
passportData.append(parsePassportData(thisPassport))

valid = invalid = 0
for passport in passportData:
    passes = True
    for field in requiredFields:
        if not field in passport:
            if field != "cid":
                passes = False
    if passes:
        valid += 1
    else:
        invalid += 1 

print(f"Valid: {valid}")
print(f"Invalid: {invalid}")
