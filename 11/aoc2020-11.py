# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:58:54 2020

@author: eateren
"""

datafile = "tdata.txt"
tdata = "tdata.txt"

def readData(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]

    
    return list

data = readData(datafile)


def seatLogic(data):
    
    oldSeatLayout = data
    newSeatLayout = []
    
    for rowNo, oldRow in enumerate(oldSeatLayout):
        
        newRow = []
        
        for seatNo, seat in enumerate(oldRow):
            
            
            adjSeats = []
            
            for y in range(-1,2):
                
                if (rowNo == 0 and y == -1) or (rowNo == len(oldSeatLayout) - 1 and y == 1):
                    continue
                else:
                    checkRow = oldSeatLayout[rowNo + y]
                                    
                for x in range(-1,2):
                    
                    if (seatNo == 0 and x == -1) or (seatNo == len(checkRow) - 1 and x == 1):
                        continue
                    else:
                        adjSeats.append(checkRow[seatNo + x])

                        
                
            if oldSeatLayout[rowNo][seatNo] == ".":
                newRow.append(oldSeatLayout[rowNo][seatNo])
            elif "#" not in adjSeats:
                newRow.append("#")
            elif adjSeats.count("#") > 4:
                newRow.append("L")
            else:
                newRow.append(oldSeatLayout[rowNo][seatNo])
                


        newSeatLayout.append(newRow)
        
    return newSeatLayout
                

def fillSeats(data):
    
    oldSet = data
    newSet = []
                        
    while oldSet != newSet:
        
        oldSet = data
        data = seatLogic(data)
        newSet = data
        
    return data
                        
                        
finalData = fillSeats(data)

def countSeats(finalData):
    
    seatCount = 0
    for line in finalData:
        seatCount += line.count("#")
    
    return seatCount


# Part two


def listifyData(data):
    
    listData = []
    for line in data:
        lineData = []
        for item in line:
            lineData.append(item)
        listData.append(lineData)
    
    return listData


listData = listifyData(data)
def seatLogic2(data):
    
    oldSeatLayout = data
    newSeatLayout = []
    
    for rowNo, oldRow in enumerate(oldSeatLayout):
        
        newRow = []
        
        for seatNo, seat in enumerate(oldRow):
            
            
            adjSeats = []
            
            for y in range(-1,2):
             
                for x in range(-1,2):
                    
                    vectorLength = 1

                    while True:

                        skipAdj = False
                        adjRowNo = rowNo + (y * vectorLength)
                        adjSeatNo = seatNo + (x * vectorLength)
                        print(adjSeatNo)
                        print(seatNo)


                        adjRowChk = adjRowNo not in range(0, len(oldSeatLayout))
                        adjSeatChk = adjSeatNo not in range(0, len(oldRow))
                        centerAdj = (x == 0) and (y == 0)
                        print(adjSeatChk)
                        
                        
                        if centerAdj:
                            skipAdj = True
                            print("center")
                            break
                        
                        if (adjRowChk or adjSeatChk) and (vectorLength == 1):
                            skipAdj = True
                            print("edgE")
                            break


                        if adjRowChk:
                            adjRowNo = rowNo + (y * (vectorLength - 1))
                            
                        if adjSeatChk:
                            adjSeatNo = seatNo + (x * (vectorLength - 1))
                            

                        
                        
                        print(adjRowNo, adjSeatNo)
                        print("space: ", oldSeatLayout[adjRowNo][adjSeatNo])
                        if oldSeatLayout[adjRowNo][adjSeatNo] == "." and (not (adjRowChk or adjSeatChk)):
                            vectorLength += 1
                            print("vector: ", vectorLength)
                        else:
                            break
                            
                    if skipAdj:
                        continue
                    
                    adjSeats.append(oldSeatLayout[adjRowNo][adjSeatNo])
                    
                    
                        
                        
            print(adjSeats)
            if oldSeatLayout[rowNo][seatNo] == ".":
                newRow.append(oldSeatLayout[rowNo][seatNo])
            elif "#" not in adjSeats:
                newRow.append("#")
            elif adjSeats.count("#") > 4:
                newRow.append("L")
            else:
                newRow.append(oldSeatLayout[rowNo][seatNo])
                


        newSeatLayout.append(newRow)
        
    return newSeatLayout

                

def fillSeats2(listData):
    
    oldSet = listData
    newSet = []
                     
    x = 0
    while oldSet != newSet:
        
        
        oldSet = listData.copy()
        listData = seatLogic2(listData).copy()
        newSet = listData.copy()
        
        x += 1
        print(x)

        
    return newSet
                        
                        
finalData2 = fillSeats2(listData)

def countSeats2(finalData2):
    
    seatCount = 0
    for line in finalData2:
        seatCount += line.count("#")
    
    return seatCount