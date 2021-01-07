# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:07:43 2020

@author: eateren
"""


data = "467528193"


def formatCups(data):
    cups = []
    for n in data:
        cups.append(int(n))
    return cups


cups = formatCups(data)


def crabCups(cups):

    currCup = cups.pop(0)
    pickCups = cups[:3]
    cups = cups[3:]
    
    
    destCup = currCup - 1
    if destCup == 0:
        destCup = 9
    while destCup in pickCups:
        destCup = destCup - 1
        if destCup < 1:
            destCup = 9
    
    destIndex = cups.index(destCup) + 1
    
    cups = cups[:destIndex] + pickCups + cups[destIndex:] + [currCup]
    
    return cups


def hundredCups(cups):

    for n in range(100):
        cups = crabCups(cups)
        
    cDex = cups.index(1) + 1
    num = ""
    for n in cups[cDex:] + cups[:cDex - 1]:
        num += str(n)
    return num


print(hundredCups(cups))

# Part Two
# looking at reddit I found that moving around sets of lists 10mil times
# takes too long.  We are doing again a dictionary method!!


data2 = "467528193"


def createDict(data2):
    
    cupDict = {}
    
    for x in range(999999):
        
        if x < 9:
            key = int(data2[x])
            if x == 8:
                nextNum = 10
            else:
                nextNum = int(data2[x + 1])
        else:
            key, nextNum = x + 1, x + 2
        
        cupDict[key] = nextNum
    
    cupDict[1000000] = int(data2[0])
    return cupDict


cupDict = createDict(data2)


def cycleTenMil(cupDict):

    currCup = list(cupDict.keys())[0]
    
    def pickCups(currCup):
        
        pickedCups = []
        nextCup = cupDict[currCup]
        for x in range(3):
            
            pickedCups.append(nextCup)
            nextCup = cupDict[nextCup]

        return pickedCups
        
    for x in range(10000000):
        pickedCups = pickCups(currCup)
        
        destCup = currCup - 1
        while destCup in pickedCups or destCup <= 0:
            destCup -= 1
            if destCup <= 0:
                destCup = len(cupDict)
        
        currCupPointer = cupDict[pickedCups[-1]]
        cupDict[currCup] = currCupPointer
    
        pickCupLastPointer = cupDict[destCup]
        cupDict[pickedCups[-1]] = pickCupLastPointer
        
        destCupPointer = pickedCups[0]
        cupDict[destCup] = destCupPointer
        
        currCup = currCupPointer
        
    return cupDict


newCupDict = cycleTenMil(cupDict)

print(newCupDict[1] * newCupDict[newCupDict[1]])





