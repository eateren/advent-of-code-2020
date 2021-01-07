# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:25:01 2020

@author: eateren
"""

filename = "data.txt"


def cleanData(filename):
    
    with open(filename) as file:
        data = file.read().replace("\n", " ")

    data = data.split("  ")
        
    return data


data = cleanData(filename)


def countYeses(data):
    
    sum = 0
    ABC = "abcdefghijklmnopqrstuvwxyz"
    
    for line in data:
    
        count = 0
        for x in ABC:
            
            if x in line:
                
                count += 1
                
        sum += count
    
    print(sum)
    return sum


countYeses(data)


def splitData(data):
    
    newData = []
    
    for line in data:
        
        newList = line.split()
        newData.append(newList)
        
    return newData

newData = splitData(data)


def countY2(newData):
    
    sum = 0
    ABC = "abcdefghijklmnopqrstuvwxyz"
    
    for newList in newData:
            
        for x in ABC:
            
            itemCount = len(newList)
            itemYcount = 0
            for item in newList:
                
                if x in item:
                    
                    itemYcount +=1
                
            if itemYcount == itemCount:
                sum += 1
    print(sum)
    return sum
            
        
countY2(newData)    
        
        
        