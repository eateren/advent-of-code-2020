# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:32:04 2020

@author: eateren
"""

def readData(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [int(line.strip()) for line in list]
    
    return list

data = readData("data.txt")


def findBreak(data):
    
    numChk = True
    x = 25
    enum = 0
    while numChk == True:
        
        enum += 1
        num = data[x]
        prevNums = data[x - 25:x]

        
        count = 0
        for y, pNum in enumerate(prevNums):
            for z in range(y + 1, 25):
                
                numSum = prevNums[y] + prevNums[z]
                if numSum != num:
                    
                    count += 1

        if count == 300:
            break            
        x += 1
        
    return num

num1 = findBreak(data)
print(num1)

def findLineMin(data):
    
    minList = []
    for x, num in enumerate(data):

        minList.append(sum(data[x:x+2]))
        
    return minList

minList = findLineMin(data)


def findMaxLine(minList):
    
    for x, num in enumerate(minList):
        
        if num >= num1:
            print(x)
            break


num1Idex = data.index(num1)
        
def findrange(data):
    
    stopChk = False
    
    for x in range(0,num1Idex):
        
        for y in range(x + 1, num1Idex):
            
            chkNum = sum(data[x:y+1])
            
            if chkNum == num1:
                print(x, ", ", y + 1, min(data[x:y + 1]) + max(data[x:y + 1]))
                stopChk = True
                break
        
        if stopChk == True:

            break
            
findrange(data)           
            
        


                    
            