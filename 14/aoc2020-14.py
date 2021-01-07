# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:52:35 2020

@author: eateren
"""


datafile = "data.txt"

def readDataFile(datafile):
    
    with open(datafile) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    
    parsedList = []
    for no, line in enumerate(list):

        
        if line[:3] == "mem":
            newLine = line
            newLine = newLine.split(" = ")
            newLine[0] = newLine[0].replace("mem[", "").replace("]", "")
        else:
            newLine = line
            newLine = newLine.replace("mask = ", "")
        
        parsedList.append(newLine)
    
    return parsedList


data = readDataFile(datafile)


def processData(data):
    
    dataMem = {}
    
    for line in data:
        
        if len(line) == 36:
            mask = line
        else:
            
            memLoc = line[0]
            dataDec = int(line[1])
            dataBin = bin(dataDec)[2:].zfill(36)
            newBin = ""
            
            for x, maskDig in enumerate(mask):
                if maskDig == "X":
                    newBin += dataBin[x]
                else: 
                    newBin += mask[x]
            
            dataMem[memLoc] = newBin
    
    return dataMem
                        

dataMem = processData(data)
            

def sumNums(dataMem):
    
    sums = 0
    for line in dataMem:
        sums += int(dataMem[line],2)
    return sums

print(sumNums(dataMem))



def countMaxX(data):
    
    maxCount = 0
    for line in data:
        if len(line) == 36:
            count = line.count("X")
            if count > maxCount:
                maxCount = count
    return maxCount
            
            

def processData2(data):
    
    dataMem = {}
    
    for line in data:
        
        if len(line) == 36:
            mask = line
            
            xIndex = []
            for pos, digit in enumerate(mask):
                if digit == "X":
                    xIndex.append(pos)

        
        else:
            iterations = 2 ** len(xIndex)
            iterBinLen = len(bin(iterations)[2:])
            for x in range(iterations):
                
                maskList = bin(x)[2:].zfill(iterBinLen)
                memLoc = line[0]
                dataDec = int(line[1])
                memBin = bin(int(memLoc))[2:].zfill(36)
                newBin = ""
                
                xCount = 1
                for z, maskDig in enumerate(mask):
                    if maskDig == "X":
                        newBin += maskList[xCount]
                        xCount += 1
                    elif maskDig == "1":
                        newBin += "1"
                    else:
                        newBin += memBin[z]
                
                newLoc = int(newBin,2)
                
                dataMem[newLoc] = dataDec
            
                
    return dataMem      


dataMem2 = processData2(data)     
            

def sumNums2(dataMem2):
    
    sums = 0
    for line in dataMem2:
        sums += int(dataMem2[line])
    return sums

print(sumNums2(dataMem2))