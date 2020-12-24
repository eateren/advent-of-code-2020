# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:55:13 2020

@author: eateren
"""


datafile = "data.txt"
tdata = "tdata.txt"

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


def combindJoltDiff(data, joltDiff):
    
    combData = []
    for x in range(0, len(joltDiff)):
        
        dataline = [data[x], joltDiff[x]]
        combData.append(dataline)
        
    return combData

combData = combindJoltDiff(data, joltDiff)


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














"""
# the below algo doesnt work.  A good method is to count the groups of one 
differences to calculate the number of different groupings.
This is because the diffs in this dataset is either 1 or 3.

This solution is not ideal, but works well because of the vuneralbility of the
dataset.


"""

maxData = max(data)

def countPermutations(data):
    
    x = 0
    
    maxStepList = []
    while True:
        
        countSteps = 0
        step = x
        
        for y in range(1,4):
            print(step + y)
            
            if step + y in data:
                countSteps += 1
                x = step + y
                
        if countSteps == 3:
            countSteps = 4
        
        maxStepList.append(countSteps)
        
        if x >= maxData:
            break
        
    return maxStepList
    
maxStepList = countPermutations(data)

def findPerm(maxStepList):

    num = 1    
    for no, x in enumerate(maxStepList):
        
        num = num * x

        
    return num
    
perm = findPerm(maxStepList)
    


def test(data):
    
    for x, num in enumerate(data):
        
        print(x, num)
        if data[x+1] - num == 2:
            print(2)


    