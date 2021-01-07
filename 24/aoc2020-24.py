# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:00:01 2020

@author: eateren
"""

import re

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.readlines()
    
    regex = "(e|w|se|sw|nw|ne)"
    data = [re.findall(regex, line.strip()) for line in data]
    
    return data


data = readData(datafile)


moveDict = {
    "eE": (1, 0), "wE": (-1, 0),
    "eO": (1, 0), "wO": (-1, 0),
    "seE": (0, -1), "swE": (-1, -1),
    "neE": (0, 1), "nwE": (-1, 1),
    "seO": (1, -1), "swO": (0, -1),
    "neO": (1, 1), "nwO": (0, 1)
    }



def fileTiles(data):
    
    tileDict = {}
   
    for instructions in data:
        
        x, y = 0, 0
        for step in instructions:
            
            adj = "E" if y % 2 == 0 else "O"
            move = moveDict[step + adj]
            x += move[0]
            y += move[1]
            
        dictCoor = str(x) + "," + str(y)
        
        if dictCoor in tileDict:
            tileDict[dictCoor] = ( tileDict[dictCoor] + 1 ) % 2
        else:
            tileDict[dictCoor] = 1
            
            
    return tileDict
            

tileDict = fileTiles(data)


def findBlackTotal(tileDict):
    
    total = 0
    for tile in tileDict:
        total += tileDict[tile]
    
    return total


print(findBlackTotal(tileDict))



# part Two



def findCoorLimits(tileDict):
    
    coorList = [coor.split(",") for coor in list(tileDict.keys())]
    xList, yList = [], []
    for coorStr in coorList:
        xList.append(int(coorStr[0]))
        yList.append(int(coorStr[1]))
    
    mapLimits = [[min(xList),max(xList)], [min(yList),max(yList)]]
    
    return mapLimits



def hundredDays(tileDict):
    
    moveDir = ("e","w","se","sw","nw","ne")
    nextTileDict = tileDict.copy()
    
    for times in range(100):
        
        mapLimits = findCoorLimits(tileDict)
        for x in range(mapLimits[0][0] - 1, mapLimits[0][1] + 2):
            for y in range(mapLimits[1][0] - 1, mapLimits[1][1] + 2):

                tile = str(x) + "," + str(y)
                adj = "E" if y % 2 == 0 else "O"
                
                bCount = 0
                for direc in moveDir:
                    move = moveDict[direc + adj]
                    xChk = x + move[0]
                    yChk = y + move[1]
                    chkTile = str(xChk) + "," + str(yChk)
                    
                    if chkTile in tileDict:
                        bCount += tileDict[chkTile]
                    
                if tile not in tileDict:
                    tileCol = 0
                else:
                    tileCol = tileDict[tile]

                if tileCol == 1:
                    if bCount == 0 or bCount > 2:
                        nextTileDict[tile] = 0
                else:
                    if bCount == 2:
                        nextTileDict[tile] = 1
                        
        tileDict = nextTileDict.copy()
        
    return nextTileDict
                
    
    
newtileDict = hundredDays(tileDict)
print(findBlackTotal(newtileDict))


    
    