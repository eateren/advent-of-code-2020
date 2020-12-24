# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:25:01 2020

@author: eateren
"""

def cleanData(filename):
    
    with open(filename) as file:
        data = file.read().replace("\n", " ")
                                   
    
    data = data.split("  ")
        
    return data

def countYeses(data):
    
    sum = 0
    ABC = "abcdefghijklmnopqrstuvwxyz"
    
    for line in data:
    
        count = 0
        for x in ABC:
            
            if x in line:
                
                count += 1
                
        sum += count
    
    return sum


def splitData(data):
    
    newData = []
    
    for line in data:
        
        newList = line.split()
        newData.append(newList)
        
    return newData


def countY2(data):
    
    sum = 0
    ABC = "abcdefghijklmnopqrstuvwxyz"
    
    for newList in data:
            
        for x in ABC:
            
            itemCount = len(newList)
            itemYcount = 0
            for item in newList:
                
                if x in item:
                    
                    itemYcount +=1
                
            if itemYcount == itemCount:
                sum += 1
    
    return sum
            
        
        
        
        
        