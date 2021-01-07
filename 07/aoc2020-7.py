# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:57:10 2020

@author: eateren
"""



import numpy as np 
  
# function to get unique values 
def unique(list1): 
    x = np.array(list1) 
    return(np.unique(x))
    print(np.unique(x)) 

filename = "data.txt"

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


newData = dataReader(filename)
newData = cleanData(newData)



def findNoBags(newData):
    
    bagList = ["shiny gold bag"]
    checkedBagList = []
    
    bagListLen = len(bagList)
    bagListLenCheck = 0
    
    while not bagListLen == bagListLenCheck:
   
        for x, bagListItem in enumerate(bagList):
           
            if bagListItem in checkedBagList:
                continue
            
            checkedBagList.append(bagListItem)
            
            for y, lineBagData in enumerate(newData):
                
                if bagListItem in lineBagData[1]:
                    
                    if lineBagData[0] not in bagList:
                        
                        bagList.append(lineBagData[0])
                    
        bagListLenCheck = len(bagList)

        print("num of bags:",len(bagList) - 1)
        
        return len(bagList) - 1


findNoBags(newData)



# split list further
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


def getCount(bag):
    
    count = countBagsIn(bag)
    print(count)


cleanedData = dataReader2("data.txt")
getCount("shiny gold bag")


