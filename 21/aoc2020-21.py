# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:38:14 2020

@author: eateren
"""


datafile = "data.txt"


def readData(datafile):
    
    with open(datafile) as file:
        data = file.readlines()
        
    ingrList = [line[:line.find(" (")].split(" ") for line in data]
    allerList = [line.strip()[line.find(" (") + 11:-1].split(", ") for line in data]
    
    return ingrList, allerList

ingrList, allerList = readData(datafile)


def createAllerDict(ingrList, allerList):
    
    
    allerDict = {}
    
    
    for listNo, allerGroup in enumerate(allerList):
        for allergen in allerGroup:
            
            if allergen not in allerDict:

                allerDict[allergen] = ingrList[listNo]
                
            else:
                
                ingrGroup = []
                for ingr in ingrList[listNo]:
                    if ingr in allerDict[allergen]:
                        ingrGroup.append(ingr)
                allerDict[allergen] = ingrGroup

    return allerDict


allerDict = createAllerDict(ingrList, allerList)


def countIngr(allerDict):
    
    ingrCounts = {}
    for allergen in allerDict:
        for ingr in allerDict[allergen]:
            if ingr not in ingrCounts:
                ingrCounts[ingr] = 0
            else:
                ingrCounts[ingr] += 1
    
    return ingrCounts
    

def idAller(allerDict):
    
    ingrAller = {}
    ingrCounts = countIngr(allerDict)
    allerDictCopy = allerDict.copy()
    
    while len(ingrCounts) > 0:
        
        for ingr in ingrCounts:
            startover = False
            if ingrCounts[ingr] == 0:
                
                for aller in allerDictCopy:
                    if ingr in allerDictCopy[aller]:
                        allerDictCopy.pop(aller)
                        ingrCounts.pop(ingr)
                        ingrAller[ingr] = aller
                        ingrCounts = countIngr(allerDictCopy)
                        startover = True
                        break
            if startover == True:
                break
            
    return ingrAller
            
ingrAller = idAller(allerDict)
    
def safeIngrCount(ingrAller, ingrList):
    
    count = 0
    for ingrGroup in ingrList:
        for ingr in ingrGroup:
            if ingr not in ingrAller:
                count += 1
                
    return count

def createCDIL(ingrAller):
    
    ingrAller = sorted(ingrAller.items(), key = lambda sortvalue: sortvalue[1])
    
    CDIL = [ingr[0] for ingr in ingrAller]
        
    return ",".join(CDIL)