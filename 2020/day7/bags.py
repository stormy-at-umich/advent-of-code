import re

class BagCollection:

    def __init__(self):
        self.bags = {}

    def dataToBags(self,data):

        # This one parses the subject from the objects
        regExOne = r"^([a-z ]+)\sbags contain\s(.*)\.$"

        # This one parses the object into a color and a quantity
        regExTwo = r"^(\d+) (.*) bags?$"

        for line in data:

            match = re.match(regExOne,line)
            newBagColor = match.group(1)
            bagContents = match.group(2)

            newBag = self.addBag(newBagColor)

            if bagContents != "no other bags":

                subBags = bagContents.split(', ')
                for subBag in subBags:
                    subBagMatch = re.match(regExTwo,subBag)
                    quantity = int(subBagMatch.group(1))
                    color = subBagMatch.group(2)
                    newBag.addChild(color,quantity)
                    self.addBag(color).addParent(newBagColor)

    def addBag(self,color):
        if color not in self.bags:
            newBag = Bag(color)
            self.bags[color] = newBag
        else:
            newBag = self.bags[color]
        return(newBag)

    def getBags(self):
        return(self.bags)

    def getAncestors(self,color):
        thisBag = self.bags[color]
        parents = thisBag.getParents() 
        ancestors = []
        for parent in parents:
            grandparentsSet = self.getAncestors(parent)
            for grandparent in grandparentsSet:
                if not grandparent in ancestors:
                    ancestors.append(grandparent)
            if not parent in ancestors:
                ancestors.append(parent)
        return(ancestors)

    def tallyContents(self,seed):
        tally = 0
        children = self.bags[seed].getChildren()
        for child in children:
            tally += children[child]
            descendantTally = self.tallyContents(child)
            if (descendantTally):
                tally += children[child] * descendantTally
        return(tally)

class Bag:

    def __init__(self,color,parentColor=False):
        self.parents = []
        self.children = {}
        self.color = color

    def addParent(self,color):
        if not color in self.parents:
            self.parents.append(color)

    def addChild(self,color,quantity):
        try:
            self.children[color] += quantity
        except(KeyError):
            self.children[color] = quantity

    def getParents(self):
        return self.parents

    def getChildren(self):
        return self.children

