# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:58 2020

@author: eateren
"""

def findGoodPasswords(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    
    list = [line.strip() for line in list]
    
    list = [line.replace("-", " ") for line in list]
    
    list = [line.split() for line in list]
    
    for line in list:
        line[2] = line[2].replace(":", "")
    
    count = 0
    for line in list:
        if line[3].count(line[2]) >= int(line[0]) and line[3].count(line[2]) <= int(line[1]):
            count += 1

    
    return count
    



def findGoodPasswords2(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    
    list = [line.strip() for line in list]
    
    list = [line.replace("-", " ") for line in list]
    
    list = [line.split() for line in list]
    
    for line in list:
        line[2] = line[2].replace(":", "")
    
    count = 0
    for line in list:

        print(line)
        
        char = line[2]
        print(char)
        
        pos1Char = line[3][int(line[0]) - 1 ]
        print(pos1Char)
        
        pos2Char = line[3][int(line[1]) - 1 ]
        print(pos2Char)
        
        
        if (char == pos1Char) is not (char == pos2Char):
            count += 1

    
    return count