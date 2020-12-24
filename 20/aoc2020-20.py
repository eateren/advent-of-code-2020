# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:43:02 2020

@author: eateren
"""

# for part one I think all we need to do if file the tiles that have two sides
# that dont match to other tile sides.


# read data

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.read()
        
    data = [line.split("\n") for line in data.split("\n\n")]

    return data
    

data = readData(datafile)

def createSideDict(data):
    
    sideDict = {}
    
    for tile in data:
        
        tileKey = int(tile[0][-5:-1])
        matchTiles = []
        
        for x in [1,10]:
            
            # first and last row
            matchTiles.append(tile[x])
            
            revTile = "".join(list(reversed(tile[x])))
            matchTiles.append(revTile)
            
            # columns
            col = ""
            for row in tile[1:]:
                col += row[x-1]
                
            matchTiles.append(col)
            
            revCol = "".join(list(reversed(col)))
            matchTiles.append(revCol)
        

        
        sideDict[tileKey] = matchTiles
        
    return sideDict

sideDict = createSideDict(data)



def findTileSideMatches(tileSides, sideDict):
    
    count = 0
    for side in tileSides:
        for otherSides in sideDict:
            if side in sideDict[otherSides]:
                count += 1
    
    return count


def listSideMatches(sideDict):
    
    sideMatches = {}
    for tileKey in sideDict:
        sideMatches[tileKey] = findTileSideMatches(sideDict[tileKey], sideDict)

    return sideMatches
    
sideMatches = listSideMatches(sideDict)
    
def findProduct(sideMatches):
    
    product = 1
    
    for key in sideMatches:
        
        if sideMatches[key] == 12:
            
            product *= key
    
    return product