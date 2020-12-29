# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:43:02 2020

@author: eateren
"""
from pprint import pprint


# for part one I think all we need to do if file the tiles that have two sides
# that dont match to other tile sides.


# read data

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.read()
        
    data = [line.split("\n") for line in data.split("\n\n")]
    
    tileDict = {}
    for tile in data:
        tileKey = int(tile[0][-5:-1])
        tileDict[tileKey] = tile[1:11]
    
    
    return tileDict
    
tileDict = readData(datafile)



def findTileSides(tileKey, tileDict):

        matchTiles = []
        
        for x in [0,9]:
            
            # first and last row
            matchTiles.append(tileDict[tileKey][x])
            
            revTile = "".join(list(reversed(tileDict[tileKey][x])))
            matchTiles.append(revTile)
            
            # columns
            col = ""
            for row in tileDict[tileKey]:
                col += row[x]
                
            matchTiles.append(col)
            
            revCol = "".join(list(reversed(col)))
            matchTiles.append(revCol)
        
        return matchTiles




def createSideDict(tileDict):
    
    sideDict = {}
    
    for tileKey in tileDict:

        sideDict[tileKey] = findTileSides(tileKey, tileDict)
        
    return sideDict

sideDict = createSideDict(tileDict)



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




# part two requires that the tiles be matched to an image..
# make a list of corners, sides, and full-tiles
# start with a corner, then piece together sides until corner.  len = 12
# continue until coordinates set
# remove borders then create image

def createTileLists(tileDict, sideMatches):
    
    tileCornerList = {}
    tileSideList = {}
    tileFullList = {}

    for match in sideMatches:
        
        matchCo = sideMatches[match]
        
        if matchCo == 12:
            tileCornerList[match] = tileDict[match]       
        elif matchCo == 14:
            tileSideList[match] = tileDict[match]
        elif matchCo == 16:
            tileFullList[match] = tileDict[match]
        
    return tileCornerList, tileSideList, tileFullList

tileCornerList, tileSideList, tileFullList = createTileLists(tileDict, sideMatches)


def rotateTile(tile):
    
    newTile = []
    for rNo, row in enumerate(tile):
        for sNo, square in enumerate(row):
            
            if rNo == 0:
                newTile.append("")
                newTile[sNo] = ""
            
            newTile[sNo] = square + newTile[sNo]
    return newTile


def flipTile(tile):
    
    newTile = []
    for rNo, row in enumerate(tile):
        newTile.append(row[::-1])
    return newTile


def matchRightSide(tileKey, sideDict, tileDict):
    
    sideDictCopy = sideDict.copy()
    rightSide = sideDictCopy[tileKey][6]
    del sideDictCopy[tileKey]
    
    # find the tile that matches
    for matchTileKey in sideDictCopy:
        
        for rowNo, row in enumerate(sideDictCopy[matchTileKey]):
            
            if row == rightSide:
                matchRowNo = rowNo
                newTile = tileDict[matchTileKey]
                newTileKey = matchTileKey
          
    # flip, rotate the tile to match up
    turnsList = [
        [1, 3],
        [0, 3],
        [0, 0],
        [1, 2],
        [0, 1],
        [1, 1],
        [1, 0],
        [0, 2],
        ]
    
    flipCount = turnsList[matchRowNo][0]
    rotCount = turnsList[matchRowNo][1]
    
    if flipCount == 1:
        newTile = flipTile(newTile)
    
    for x in range(rotCount):
        newTile = rotateTile(newTile)
        
    return matchRowNo, newTileKey, newTile
    
    
    
def matchBotSide(tileKey, sideDict, tileDict):
    
    sideDictCopy = sideDict.copy()
    botSide = sideDictCopy[tileKey][4]
    del sideDictCopy[tileKey]
    
    # find the tile that matches
    for matchTileKey in sideDictCopy:
        
        for rowNo, row in enumerate(sideDictCopy[matchTileKey]):
            
            if row == botSide:
                matchRowNo = rowNo
                newTile = tileDict[matchTileKey]
                newTileKey = matchTileKey

    # flip, rotate the tile to match up
    turnsList = [
        [0, 0],
        [1, 0],
        [1, 3],
        [0, 1],
        [1, 2],
        [0, 2],
        [0, 3],
        [1, 1]
        ]
    
    flipCount = turnsList[matchRowNo][0]
    rotCount = turnsList[matchRowNo][1]
    
    if flipCount == 1:
        newTile = flipTile(newTile)
    
    for x in range(rotCount):
        newTile = rotateTile(newTile)
        
    return matchRowNo, newTileKey, newTile


def findTopLeftCorner(tileCornerList):
    
    
    cornerMatches = {}
    for tileKey in tileCornerList:
        
        sideDictCopy = sideDict.copy()
        del sideDictCopy[tileKey]
        matches = []
        
        for side in sideDict[tileKey]:
            
            foundBool = 0
            for tileKey2 in sideDictCopy:
                for side2 in sideDictCopy[tileKey2]:
                    if side == side2:
                        foundBool = 1
                        
            matches.append(foundBool)
                    
        cornerMatches[tileKey] = matches
    
    pprint(cornerMatches)
        

# 1543 is a top left corner without rotating
topLeftTile = 1543


def createRawImage(topLeftTile, tileDict, sideDict):
    
    imgLen = 12
    imgHgt = 12
    imageList = []
    
    for y in range(imgHgt):
        
        
        imageRow = []
        for x in range(imgLen):
            
            if y == 0 and x == 0:
                imageRow.append(topLeftTile)
            
            elif x == 0:
                
                matchRowNo, newTileKey, newTile = matchBotSide(imageList[y-1][x], sideDict, tileDict)
                tileDict[newTileKey] = newTile
                sideDict[newTileKey] = findTileSides(newTileKey, tileDict)
                imageRow.append(newTileKey)
            
            else:
                
                matchRowNo, newTileKey, newTile = matchRightSide(imageRow[x-1], sideDict, tileDict)
                tileDict[newTileKey] = newTile
                sideDict[newTileKey] = findTileSides(newTileKey, tileDict)
                imageRow.append(newTileKey)
                
        
        imageList.append(imageRow)
        
    return imageList


rawImageList = createRawImage(topLeftTile, tileDict, sideDict)


def stitchImage(rawImageList):

    
    mapList = []
    for tileRow in rawImageList:
        
        for textRow in range(8):
            
            mapRow = ""
            for tileKey in tileRow:
                
                mapRow += tileDict[tileKey][textRow + 1][1:-1]
                
            mapList.append(mapRow)
            
    return mapList


testImage = """.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###""".split("\n")

testImage = rotateTile(testImage)
testImage = flipTile(testImage)

mapImage = stitchImage(rawImageList)
mapImage = rotateTile(mapImage)
mapImage = rotateTile(mapImage)

"""
kept flipping map until found matches
mapImage = flipTile(mapImage)
mapImage = rotateTile(mapImage)
"""


seaMonster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """

def seaMonsterPos(seaMonster, mapImage):
    
    smList = seaMonster.split("\n")
    smIndex = []
    for row in smList:
        rowDex = []
        for charNo, char in enumerate(row):
            if char == "#":
                rowDex.append(charNo)
        smIndex.append(rowDex)
                
    
    
    widSearchLen = len(mapImage) - 20 + 1
    hgtSearchLen = len(mapImage) - 3 + 1
    smPosList = []
    
    
    for y in range(hgtSearchLen):

        for x in range(widSearchLen):

            checkArea = [
                mapImage[y][x:x + 20],
                mapImage[y + 1][x:x + 20],
                mapImage[y + 2][x:x + 20]
                ]

            checkList = []
            for mYNo, mY in enumerate(smIndex):
                for mX in mY:
                    checkList.append(checkArea[mYNo][mX] == "#")
            

            if all(checkList):
                smPosList.append([x,y])
                print(checkList)
    
    print(smPosList)
    return smPosList
    
    
def countChoppy(mapImage):
    
    count = 0
    
    for y in mapImage:
        for x in y:
            if x == "#":
                count += 1
                
    return count - len(seaMonsterPos(seaMonster, mapImage) * 15)
    