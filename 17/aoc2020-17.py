# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:41:50 2020

@author: eateren
"""


datafile = "data.txt"


def initCube(datafile):
    
    x, y, z = 0, 0, 0
    
    with open(datafile) as file:
        list = file.readlines()
        
    space = {}
    
    for y, line in enumerate(list):
        
        for x, state in enumerate(line.strip()):
            
            posKey = (x, y, z)
            
            space[posKey] = state
            
    return space


space = initCube(datafile)


def findSpaceDim(space):
    
    minDim = [0, 0, 0]
    maxDim = [0, 0, 0]

    
    for key in space.keys():
        
        for dim in range(3):
        
            if key[dim] < minDim[dim]:
                minDim[dim] = key[dim]
            elif key[dim] > maxDim[dim]:
                maxDim[dim] = key[dim]
    
    return minDim, maxDim
            

def printSpace(newSpace):
    
    spaceDim = findSpaceDim(newSpace)

    for z in range(spaceDim[0][2], spaceDim[1][2] + 1):
        
        zSpace = ""
        for y in range(spaceDim[0][1], spaceDim[1][1] + 1):
            
            line = ""
            for x in range(spaceDim[0][0], spaceDim[1][0] + 1):
                
                try:
                    state = newSpace[x, y, z]
                except:
                    state = "."
                
                line += state
            
            zSpace += line + "\n"



def cycleCubes(space):
    
    newSpace = space.copy()
    
    for cycle in range(6):
        
        spaceDim = findSpaceDim(newSpace)
        newSpaceOld = newSpace.copy()
        
        for x in range(spaceDim[0][0] - 1, spaceDim[1][0] + 2):
            
            for y in range(spaceDim[0][1] - 1, spaceDim[1][1] + 2):
                
                for z in range(spaceDim[0][2] - 1, spaceDim[1][2] + 2):
                    
                    try:
                        state = newSpaceOld[(x, y, z)]
                    except:
                        state = "."
                        pass
                        
                    activeCount = 0
                    for xChk in range(x - 1, x + 2):
                          
                        for yChk in range(y - 1, y + 2):
                            
                            for zChk in range(z - 1, z + 2):
                                
                                if xChk == x and yChk == y and zChk == z:
                                    continue
                                
                                try:
                                    chkState = newSpaceOld[(xChk, yChk, zChk)]
                                except:
                                    chkState = "."
                                    
                                
                                if chkState == "#":
                                    
                                    activeCount += 1
                                    
                    if state == "#":
                        
                        if activeCount == 2 or activeCount == 3:
                            newSpace[(x, y, z)] = "#"
                        else:
                            newSpace[(x, y, z)] = "."
                   
                    elif state == ".":
                        
                        if activeCount == 3:
                            newSpace[(x, y, z)] = "#"
        
    return newSpace


newSpace = cycleCubes(space)
                                
                                
                                
def countActives(newSpace):
    
    count = 0
    for cube in newSpace:
        
        if newSpace[cube] == "#":
            
            count += 1
    
    print(count)
    return count
                

countActives(newSpace)


"""
PART TWO
"""



def initCubeHyp(datafile):
    
    x, y, z, w= 0, 0, 0, 0
    
    with open(datafile) as file:
        list = file.readlines()
        
    space = {}
    
    for y, line in enumerate(list):
        
        for x, state in enumerate(line.strip()):
            
            posKey = (x, y, z, w)
            
            space[posKey] = state
            
    return space

spaceHyp = initCubeHyp(datafile)





def findSpaceDimHyp(spaceHyp):
    
    minDim = [0, 0, 0, 0]
    maxDim = [0, 0, 0, 0]

    for key in spaceHyp.keys():
        
        for dim in range(4):
        
            if key[dim] < minDim[dim]:
                minDim[dim] = key[dim]
            elif key[dim] > maxDim[dim]:
                maxDim[dim] = key[dim]
    
    return minDim, maxDim



def printSpaceHyp(newSpace):
    
    spaceDim = findSpaceDimHyp(newSpace)

    for w in range(spaceDim[0][3], spaceDim[1][3] + 1):
        
        for z in range(spaceDim[0][2], spaceDim[1][2] + 1):
            
            zSpace = ""
            for y in range(spaceDim[0][1], spaceDim[1][1] + 1):
                
                line = ""
                for x in range(spaceDim[0][0], spaceDim[1][0] + 1):
                    
                    try:
                        state = newSpace[x, y, z, w]
                    except:
                        state = "."
                    
                    line += state
                
                zSpace += line + "\n"


def cycleCubesHyp(spaceHyp):
    
    newSpace = spaceHyp.copy()
    
    for cycle in range(6):
        
        spaceDim = findSpaceDimHyp(newSpace)
        newSpaceOld = newSpace.copy()
        
        for x in range(spaceDim[0][0] - 1, spaceDim[1][0] + 2):
            
            for y in range(spaceDim[0][1] - 1, spaceDim[1][1] + 2):
                
                for z in range(spaceDim[0][2] - 1, spaceDim[1][2] + 2):
                    
                    for w in range(spaceDim[0][3] - 1, spaceDim[1][3] + 2):
                        
                        try:
                            state = newSpaceOld[(x, y, z, w)]
                        except:
                            state = "."
                            pass
                            
                        activeCount = 0
                        for xChk in range(x - 1, x + 2):
                              
                            for yChk in range(y - 1, y + 2):
                                
                                for zChk in range(z - 1, z + 2):
                                    
                                    for wChk in range(w - 1, w + 2):
                                        
                                        if xChk == x and yChk == y and zChk == z and wChk == w:
                                            continue
                                        
                                        try:
                                            chkState = newSpaceOld[(xChk, yChk, zChk, wChk)]
                                        except:
                                            chkState = "."
                                            
                                        if chkState == "#":
                                            
                                            activeCount += 1
                                        
                        if state == "#":
                            
                            if activeCount == 2 or activeCount == 3:
                                newSpace[(x, y, z, w)] = "#"
                            else:
                                newSpace[(x, y, z, w)] = "."
                       
                        elif state == ".":
                            
                            if activeCount == 3:
                                newSpace[(x, y, z, w)] = "#"
                            
        printSpaceHyp(newSpace)
                         
    return newSpace
                
                
newSpaceHyp = cycleCubesHyp(spaceHyp)

countActives(newSpaceHyp)