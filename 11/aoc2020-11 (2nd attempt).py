# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:58:54 2020

@author: eateren
"""



datafile = "data.txt"
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



def findAdjSeat(data, y, x, rowNo, seatNo):
    
    vectorLength = 1
    skipSeat = False
    foundSeat = False
    
    
    while True:
        
        rowChange = y * vectorLength
        seatChange = x * vectorLength
        
        newRow = rowNo + rowChange
        newSeat = seatNo + seatChange
        
        
        newRowChk = newRow in range(0, len(data))
        newSeatChk = newSeat in range(0, len(data[0]))
        # print("newRow: ", newRow, "newSeat: ", newSeat, "foundSeat: ", foundSeat, "vector: ", vectorLength, "skipSeat: ", skipSeat)
        
        if not newRowChk or not newSeatChk:
            newRow = rowNo + (y * (vectorLength - 1))
            newSeat = seatNo + (x * (vectorLength - 1))
            foundSeat = True
        
        if y == 0 and x == 0:
            skipSeat = True
            return skipSeat, newRow, newSeat
            break

        if newRow == rowNo and y != 0:
            skipSeat = True
  
        if newSeat == seatNo and x != 0:
            skipSeat = True

        if foundSeat:
            return skipSeat, newRow, newSeat
            break


        if data[newRow][newSeat] == ".":
            vectorLength += 1
        else:
            foundSeat = True

        

    


listData = listifyData(data)
def seatLogic2(listData):
    
    oldSeatLayout = listData
    newSeatLayout = []
    
    for rowNo, oldRow in enumerate(oldSeatLayout):
        
        newRow = []
        
        for seatNo, seat in enumerate(oldRow):
            
            
            adjSeats = []
            
            for y in range(-1,2):
             
                for x in range(-1,2):
                    
                    
                    adjSeat = findAdjSeat(listData, y, x, rowNo, seatNo)
                    adjSeaty = adjSeat[1]
                    adjSeatx = adjSeat[2]
                    
                    if adjSeat[0]:
                        continue
                    else:                    
                        adjSeats.append(oldSeatLayout[adjSeaty][adjSeatx])
                    
                    
                        
                        
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
                     

    while oldSet != newSet:
        
        
        oldSet = listData.copy()
        listData = seatLogic2(listData).copy()
        newSet = listData.copy()

        
    return newSet
                        
                        
finalData2 = fillSeats2(listData)

def countSeats2(finalData2):
    
    seatCount = 0
    for line in finalData2:
        seatCount += line.count("#")
    
    return seatCount