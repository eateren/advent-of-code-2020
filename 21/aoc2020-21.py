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
