import re
from bags import BagCollection

with open("input.txt", "r") as f:
    data = f.read().splitlines()

bc = BagCollection()
bc.dataToBags(data)
    
lookingFor = "shiny gold"

ancestors = bc.getAncestors(lookingFor)

print(f"{lookingFor} is found in {len(ancestors)} bags")
print("Those bags are:")
for ancestor in ancestors:
   print(f"  {ancestor}")
