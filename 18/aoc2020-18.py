# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:06:21 2020

@author: eateren
"""

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.readlines()
        
    data = [item.strip().replace(" ","") for item in data]
    
    return data

data = readData(datafile)



def operation(line):
    
    total = 1
    dex = 0
    nextChar = [line[dex], dex]
    
    while nextChar[0] != ")":
        
        if dex == 0:
            dex += 1
            nextChar = [line[dex], dex]
            continue
        
        if dex == 1:
            op = "*"
        
        if nextChar[0].isnumeric():
            
            if op == "*":
                total *= int(nextChar[0])
                dex += 1
                
            elif op == "+":
                total += int(nextChar[0])
                dex += 1
                
        elif nextChar[0] == "*" or nextChar[0] == "+":
            op = nextChar[0]
            dex += 1
            
        elif nextChar[0] == "(":

            subData = operation(line[dex:])  

            if op == "*":
                total *= int(subData[0])
                dex += subData[1] + 1
                
            elif op == "+":
                total += int(subData[0])
                dex += subData[1] + 1
        
        nextChar = [line[dex], dex]

    return total, dex
    

def sumDataLine1(data):
    
    sums = 0
    
    for line in data:
        
        dataline = "(" + line + ")"
        sums += operation(dataline)[0]
    
    return sums


print(sumDataLine1(data))


def updateLine(line):
    
    newLine = "("
    for x, char in enumerate(line):
        
        if x == 0:
            newLine += "("
        
        if char == "*":
            newLine += ")*("
        elif char == "(":
            newLine += "(("
        elif char == ")":
            newLine += "))"
        else:
            newLine += char
            
    newLine += "))"
    
    return newLine
       

    
def sumDataLine2(data):
    
    sums = 0
    
    for line in data:
        
        dataline = updateLine(line)
        sums += operation(dataline)[0]
    
    return sums

print(sumDataLine2(data))