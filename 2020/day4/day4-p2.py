import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def birthYearValidator(byr):
    return((len(byr) == 4) and (int(byr) >= 1920) and (int(byr) <= 2002))

def issueYearValidator(iyr):
    return((len(iyr) == 4) and (int(iyr) >= 2010) and (int(iyr) <= 2020))

def expirationYearValidator(eyr):
    return((len(eyr) == 4) and (int(eyr) >= 2020) and (int(eyr) <= 2030))

def heightValidator(hgt):
    unit = "cm"
    if "in" in hgt:
        unit = "in"
    value = int(re.sub("[^0-9]","",hgt))
    if unit == "cm":
        return((value >= 150) and (value <= 193))
    else:
        return((value >= 59) and (value <= 76))

def hairColorValidator(hcl):
    return(bool(re.match(r"^#[0-9a-f]{6}$",hcl)))
    
def eyeColorValidator(ecl):
    return(bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$",ecl)))

def passportIdValidator(pid):
    return(bool(re.match(r"^\d{9}$",pid)))

def countryIdValidator(cid):
    return(True)

requiredFields = {
    "byr" : birthYearValidator,
    "iyr" : issueYearValidator,
    "eyr" : expirationYearValidator,
    "hgt" : heightValidator,
    "hcl" : hairColorValidator,
    "ecl" : eyeColorValidator,
    "pid" : passportIdValidator,
    "cid" : countryIdValidator
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
        else:
            validFormat = requiredFields[field](passport[field])
            if (not validFormat):
                print(f"{passport[field]} failed {field} validation")
                passes = False
    if passes:
        valid += 1
    else:
        invalid += 1 

print(f"Valid: {valid}")
print(f"Invalid: {invalid}")
