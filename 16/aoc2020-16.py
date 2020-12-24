# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 11:06:14 2020

@author: eateren
"""


datafile = "data.txt"


def getRanges(datafile):
    
    with open(datafile) as file:
        list = file.readlines()

    paramList = []
    for line in list:

        if line == "\n":
            break
        
        newLine = line[line.index(": ") + 2:].strip().replace(" or ", "-").split("-")
        
        newLine = [int(i) for i in newLine]
        
        paramList.append(newLine)
        

    return paramList

paramList = getRanges(datafile)


yourTicket = [71,127,181,179,113,109,79,151,97,107,53,193,73,83,191,101,89,149,103,197]


def getNearbyTickets(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    nearbyTickets = []
    parseLine = False
    for line in list:

        if parseLine:
            newLine = line.split(",")
            newLine = [int(i) for i in newLine]
            nearbyTickets.append(newLine)
        
        if line == "nearby tickets:\n":
            parseLine = True
            
    return nearbyTickets
        
    
nearbyTickets = getNearbyTickets(datafile)


def defineAvailParam(paramList):
    
    availParam =  []
    for line in paramList:
        
        for x in range(line[0], line[1] + 1):
            availParam.append(x)
        
        for y in range(line[2], line[3] + 1):
            availParam.append(y)
        
    return availParam


availParam = defineAvailParam(paramList)

def findErrorRate(nearbyTickets, availParam):
    
    errorRate = 0
    
    for ticket in nearbyTickets:
        
        for x in ticket:
                
            errorRate += x if x not in availParam else 0
    
    return errorRate
            

# part 2
def removeInvalidTickets(nearbyTickets, availParam):
    
    validTickets = []
    
    for ticket in nearbyTickets:
        
        valid = True
        for x in ticket:
            
            valid *= False if x not in availParam else True
        
        if valid:
            validTickets.append(ticket)

    return validTickets


validTickets = removeInvalidTickets(nearbyTickets, availParam)


# having a hard time with so much permutations.
# looked up on reddit and going to try process of elimination
# https://www.youtube.com/watch?v=ZEL3hJp6qW8


allTickets = nearbyTickets.copy()
allTickets.append(yourTicket)

def cleanAllTickets(allTickets, availParam):
    
    
    newTickList = []
    for ticket in allTickets:
        
        saveTick = True
        for x in ticket:
            if x not in availParam:
                saveTick = False
        
        if saveTick:
            newTickList.append(ticket)
            
    return newTickList
    
newTickList = cleanAllTickets(allTickets, availParam)



def findTickDataPos(newTickList, paramList):
    
   
    
    dataDexFitsParams = []
    for dataDex in range(len(newTickList[0])):
        
        fitList = []
        for paramNo, params in enumerate(paramList):
        
            dataDexFit = True
            for tickNo, ticket in enumerate(newTickList): 
        
                pOneFit = params[0] <= ticket[dataDex] <= params[1]
                pTwoFit = params[2] <= ticket[dataDex] <= params[3]  
            
                if not (pOneFit or pTwoFit):
                    dataDexFit = False
                    break
            
            if dataDexFit:
                fitList.append(paramNo)
        
        dataDexFitsParams.append(fitList)
        

    return dataDexFitsParams
    
                
dataDexFitsParams = findTickDataPos(newTickList, paramList)


def findParamPos(dataDexFitsParams):
    
    paramKey = {}
    while len(paramKey) < 20:
        
        data = dataDexFitsParams.copy()
        
        for x, fitsList in enumerate(data):
            
            if len(fitsList) == 1:
                tickPos = fitsList[0]
                paramKey[tickPos] = x
                break
        
        for y, fitsList in enumerate(data):
            
            try:
                fitsList.remove(tickPos)
            except:
                pass
            
        
            
    return paramKey
        
paramKey = findParamPos(dataDexFitsParams)



def findTicketKey(yourTicket, paramKey):
    
    s = 1    
    for x in range(6):
        
        s *= yourTicket[paramKey[x]]
    
    return s
    