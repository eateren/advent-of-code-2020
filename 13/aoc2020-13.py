# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:32:59 2020

@author: eateren
"""



datafile = "data.txt"

def readDataFile(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    startTime = int(list[0].strip())
    busList = list[1].split(",")
    
    return startTime, busList

data = readDataFile(datafile)

def createBusTable(data):
    
    
    busTable = []
    
    for bus in data[1]:
        
        busTimes = []
        
        try:
            busNo = int(bus)
        except:
            continue
        
        time = 0
        while True:
            
            time += busNo
            
            busTimes.append(time)
            
            if time >= data[0]:
                break
        
        busTable.append(busTimes)
        
    return busTable
            
busTable = createBusTable(data)

def findBus(busTable):
    
    busArrivals = []
    busList = []
    
    for busTimes in busTable:
        
        busList.append(busTimes[0])
        busArrivals.append(busTimes[-1])
        
    minTime = min(busArrivals)
    
    
    return minTime, busList[busArrivals.index(minTime)]

nextBus = findBus(busTable)

print(nextBus[0] - data[0], nextBus[1], nextBus[1] * (nextBus[0] - data[0]))
            


def makeBusOffsetList(data):
    
    busOffsetList = []
    for x, bus in enumerate(data[1]):
        
        but = []
        try:
            busNo = int(bus)
        except:
            continue
    
        bus = x, busNo
    
        busOffsetList.append(bus)
    
    return busOffsetList


busOffsetList = makeBusOffsetList(data)


def findTime(busOffsetList):  #had to get help on the LCM stuff from reddit for this
    
    
    lcm = 1 # least common multiple.  This will speed up iteration
    time = 0
    busList = busOffsetList
    
    for x in range(len(busList) - 1):
        
        newDex = busList[x + 1][0]
        newBus = busList[x + 1][1]
        oldBus = busList[x][1]
        lcm *= oldBus
        
        
        while (time + newDex) % newBus != 0:
            time += lcm
    
    print(time)
    
    
    
    
    



# No Bueno
def firstTwoBusList(data):
    
    minNo = 100000000000000
    busOne = 557
    busTwo = 419
    
    busOneRem = minNo % int(busOne)
    busTwoRem = minNo % int(busTwo)
    nextBusDiff = busTwo - busOne
    
    firstTwoBusList = []
    
    busOneTime = minNo + ( busOne - busOneRem )
    busTwoTime = minNo + ( busTwo - busTwoRem )
    
    busOneList = []
    for x in range(0, 100000):
        
        busOneList.append(busOneTime)
        busOneTime += busOne
    
    busTwoList = []
    for x in range(0, 100000):
        
        busTwoList.append(busTwoTime)
        busTwoTime += busTwo
    
    return busOneList, busTwoList

firstTwoBusList = firstTwoBusList(data)

def findTwoBusDiffList(firstTwoBusList):
    
    
    busOne = 557
    busTwo = 419
    nextBusDiff = busTwo - busOne
    
    busOneMatchList = []
    for timeTwo in firstTwoBusList[1]:
        
        for timeOne in firstTwoBusList[1]:
            
            if timeTwo - timeOne == nextBusDiff:
                
                busOneMatchList.append(timeOne)
                
    return busOneMatchList
                

    
    
            