# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:57:10 2020

@author: eateren
"""


def dataReader(filename):
    
    with open(filename) as file:
        list = file.readlines()
    
    newData = []
    list = [line.strip() for line in list]
    newData = [line.split(" contain ") for line in list]

    return newData

def cleanData(data):
    
    for no, line in enumerate(data):
        
        data[no][0] = line[0].replace("bags", "bag")
        data[no][1] = line[1].replace("bags", "bag")
    
    return data

def findNoBags(newData):
    
    bagList = ["shiny gold bag"]
    checkedBagList = []
    
    bagListLen = len(bagList)
    
    while True:
   
        for x, bagListItem in enumerate(bagList):
           
            if bagListItem in checkedBagList:
                continue
            
            checkedBagList.append(bagListItem)
            
            for y, lineBagData in enumerate(newData):
                
                if bagListItem in lineBagData[1]:
                    
                    bagList.append(lineBagData[0])
                    
        bagListLenCheck = len(bagList)
        
        if bagListLen == bagListLenCheck:
            break
        
        print(bagList)
        
        return bagList
   



def dataReader2(filename):
    
    with open(filename) as file:
        list = file.readlines()
    
    newData = []
    list = [line.strip() for line in list]
    newData = [line.replace(" contain ",", ").replace("bags", "bag").replace(".","").split(", ") for line in list]

    newData2 = []
    for line in newData:

        newLine = []
        for item in line:
            
            noOfBags = 1
            bagType = item
            try:
                noOfBags = int(item[:item.find(" ")])
                bagType = item.replace(str(noOfBags) + " ", "")
            except:
                pass

            for x in range(0,noOfBags):

                newLine.append(bagType)
                
        newData2.append(newLine)

    return newData2



bagCount = 0  
def countBagsIn(bag):

    global bagCount
    bagIdex = 0
    for bagContents in cleanedData:
        
        if bag == bagContents[0]:
            break
        bagIdex += 1
    
    bagCount += len(cleanedData[bagIdex]) - 1
    
    for bag in cleanedData[bagIdex][1:]:
        if bag[:2] == "no":
            bagCount += -1
            continue
        countBagsIn(bag)
        
    return bagCount
    
    
cleanedData = dataReader2("data.txt")
countBagsIn("shiny gold bag")



    # no bueno
def createBagContentsList(newData):
    
    contentsList1 = [line[1].replace(".","").split(", ") for line in newData]
    
    contentsList = []
    
    
    for line in contentsList1:
        
        newLine = []
        for item in line:
            
            spaceLoc = item.find(" ")
            try:
                itemCount = int(item[:spaceLoc])
            except:
                pass
            
            for x in range(0, itemCount):
                
                newLine.append(item[spaceLoc:])
        
        contentsList.append(newLine)
            
    return contentsList

# no bueno
def createBagIndex(newData):
    
    list = [] 
    for line in newData:
        
        list.append(line[0])
        
    return list


# no bueno
def countBagsInShinyBag(bag):
    
    indexList = indexList
    bagContentsList = bagContentsList

    idex = indexList.index(bag)
    
    count += len(bagContentsList[idex])
    
    for x, bag in enumerate(bagContentsList[idex]):
        countBagsInShinyBag(bag)
        
    return count
