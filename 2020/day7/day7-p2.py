import re
from bags import BagCollection

with open("input.txt", "r") as f:
    data = f.read().splitlines()

bc = BagCollection()
bc.dataToBags(data)
    
lookingFor = "shiny gold"
total = bc.tallyContents(lookingFor)
print(f"Number of bags in {lookingFor} is {total}")
