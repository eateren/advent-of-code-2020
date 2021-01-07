# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:55:13 2020

@author: eateren
"""


datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    list = [int(line.strip()) for line in list]
        
    list.sort()
    
    return list

data = readData(datafile)


def findJoltDiff(data):
    
    joltDiff = []
    for x in range(0, len(data)):
        
        if x == 0:
            joltDiff.append(data[x])
        else:
            joltDiff.append(data[x] - data[x - 1])
    
    return joltDiff

joltDiff = findJoltDiff(data)
print((joltDiff.count(1)) * (joltDiff.count(3) + 1))



def combindJoltDiff(data, joltDiff):
    
    combData = []
    for x in range(0, len(joltDiff)):
        
        dataline = [data[x], joltDiff[x]]
        combData.append(dataline)
        
    return combData

combData = combindJoltDiff(data, joltDiff)



# needed help on reddit to use the groupings of 1 method

def coundOneGroupings(combData):
    
    seqCount = 0
    groupCount = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in combData:
        
        if line[1] == 1:
            seqCount += 1
        else:
            groupCount[seqCount] += 1
            seqCount = 0
    
    return groupCount
            
groupings = coundOneGroupings(combData)
permCount = (2**groupings[2]) * (4**groupings[3]) * (7**(groupings[4]+1))
print(permCount)



    