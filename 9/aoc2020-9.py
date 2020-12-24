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
        
        print("enum", enum)
        enum += 1
        num = data[x]
        prevNums = data[x - 25:x]

        
        count = 0
        for y, pNum in enumerate(prevNums):
            for z in range(y + 1, 25):
                
                numSum = prevNums[y] + prevNums[z]
                print(numSum)
                if numSum != num:
                    
                    count += 1

        if count == 300:
            print(num)
            break            
        x += 1
        
    print(num)
    return num

num1 = findBreak(data)


def findLineMin(data):
    
    minList = []
    for x, num in enumerate(data):

        minList.append(sum(data[x:x+2]))
        
    return minList

minList = findLineMin(data)


num1 = 258585477
num1Idex = data.index(num1)

def findMaxLine(minList):
    
    for x, num in enumerate(minList):
        
        if num >= num1:
            print(x)
            break
        
        
def findrange(data):
    
    
    stopChk = False
    
    for x in range(0,num1Idex):
        
        for y in range(x + 1, num1Idex):
            
            chkNum = sum(data[x:y+1])
            
            if chkNum == num1:
                print(x, ", ", y)
                stopChk = True
                break
        
        if stopChk == True:
            break
            
                
            
        


                    
            