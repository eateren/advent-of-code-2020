# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:37:58 2020

@author: eateren
"""

def treeCount(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    
    x = 3
    y = 1
    
    startPos = 0
    
    pos = startPos
    
    count = 0
    for line in list[1:]:
        print(pos)
        pos += x
        print(pos)
        pos = pos % 31
        
        print(pos)
        if line[pos] == "#":
            print(line[pos])
            count += 1
    
        print(line)
    
    
    return count


def treeCountMult(filename, x_dist, y_dist):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    
    
    
    x = x_dist
    y = y_dist
    
    startPos = 0
    
    pos = startPos
    
    count = 0
    for z in range(y,len(list),y):
        print(pos)
        pos += x
        print(pos)
        pos = pos % 31
        
        print(pos)
        if list[z][pos] == "#":
            print(list[z][pos])
            count += 1
    
        print(list[z])
    
    
    return count