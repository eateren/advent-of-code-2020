# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 20:43:58 2020

@author: eateren
"""

filename = "data.txt"

def findGoodPasswords(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.replace("-", " ").strip().split() for line in list]
    
    for line in list:
        line[2] = line[2].replace(":", "")
    
    count = 0
    for line in list:
        if line[3].count(line[2]) >= int(line[0]) and line[3].count(line[2]) <= int(line[1]):
            count += 1

    print(count)
    return count
    
findGoodPasswords(filename)


def findGoodPasswords2(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.replace("-", " ").strip().split() for line in list]
    
    for line in list:
        line[2] = line[2].replace(":", "")
    
    count = 0
    for line in list:

        char = line[2]
        pos1Char = line[3][int(line[0]) - 1 ]
        pos2Char = line[3][int(line[1]) - 1 ]
        
        if (char == pos1Char) is not (char == pos2Char):
            count += 1

    print(count)
    return count

findGoodPasswords2(filename)