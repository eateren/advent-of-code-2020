# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:10:38 2020

@author: eateren
"""

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    list = [[line[0], int(line[1:])] for line in list]
    
    return list

data = readData(datafile)


def navigate(datafile):
    
    y = 0
    x = 0
    headingDex = 1
    
    for line in data:
        
        
        compass = ["N", "E", "S", "W"]
        degrees = [0, 90, 180, 270, 360]
        
        
        
        amount = line[1]
        heading = line[0]
        
        print(compass[headingDex])
        
        
        if heading == "F":
            heading = compass[headingDex] 
        
        
        if heading == "R":
            headingDex = (headingDex + degrees.index(amount)) % 4
            heading = compass[headingDex]
            print(compass[headingDex], "turned: R ", amount)
        elif heading == "L":
            headingDex = (headingDex - degrees.index(amount)) % 4
            heading = compass[headingDex]  
            print(compass[headingDex], "turned: L ", amount)
        elif heading == "E":
            x += amount
            print(compass[headingDex], "moved: ", amount)
        elif heading == "W":
            x -= amount
            print(compass[headingDex], "moved: ", amount)
        elif heading == "N":
            y += amount
            print(compass[headingDex], "moved: ", amount)
        elif heading == "S":
            y -= amount
            print(compass[headingDex], "moved: ", amount)
        
        
            
            
    return (y, x, abs(y) + abs(x))
            
        


def moveWayPointBy(heading, amount):
    
    y = 0
    x = 0
    
    if heading == "E":
        x += amount

tswha    elif heading == "W":
        x -= amount

    elif heading == "N":
        y += amount

    elif heading == "S":
        y -= amount

    return y, x


def rotateWayPointBy(heading, amount, waypointY, waypointX):

    if heading == "L":
        amount = 360 - amount
    
    if amount == 90:
        return (-waypointX, waypointY)
    elif amount == 180:
        return (-waypointY, -waypointX)
    elif amount == 270:
        return (waypointX, -waypointY)
    
def moveShipToWayPoint(amount, shipY, shipX, waypointY, waypointX):
    
    for times in range(0, amount):
        
        shipY += waypointY
        shipX += waypointX
    
    return shipY, shipX
    
    

def navigate2(data):
    
    shipY = 0
    shipX = 0
    waypointY = 1
    waypointX = 10
    
    for line in data:
        
        heading = line[0]
        amount = line[1]
        compass = ["N", "E", "S", "W"]
        turns = ["L", "R"]
        
        print(heading, amount)
        
        if heading in compass:
            move = moveWayPointBy(heading, amount)
            waypointY += move[0]
            waypointX += move[1]
        elif heading in turns:
            rotate = rotateWayPointBy(heading, amount, waypointY, waypointX)
            waypointY = rotate[0]
            waypointX = rotate[1]
        elif heading == "F":
            shipLoc = moveShipToWayPoint(amount, shipY, shipX, waypointY, waypointX)
            shipY = shipLoc[1]
            shipX = shipLoc[0]
            
        print("ship: ", shipY, shipX)
        print("waypoint: ", waypointY, waypointX)
            
            
    return (shipY, shipX, abs(shipY) + abs(shipX))
