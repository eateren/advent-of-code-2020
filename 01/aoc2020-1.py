# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:10:21 2020

@author: eateren
"""

filename = "data.txt"


def findTwoEntries(filename):
    
    with open(filename) as file:
        list = file.readlines()
    
    list = [int(line.strip()) for line in list]
    
    
    for x in list:
        for y in list:
            if x + y == 2020:
                print(x * y)
                return x * y


findTwoEntries(filename)


def findThreeEntries(filename):
    
    with open(filename) as file:
        list = file.readlines()
    
    list = [int(line.strip()) for line in list]
    
    
    for x in list:
        for y in list:
            for z in list:
                if x + y + z == 2020:
                    print(x * y * z)
                    return x * y * z
                
findThreeEntries(filename)