# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:37:58 2020

@author: eateren
"""

filename = "data.txt"

def treeCount(filename, x_dist, y_dist):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    
    x = x_dist
    y = y_dist
    
    startPos = 0
    
    pos = startPos
    
    count = 0
    for z in range(y,len(list),y):
        pos += x
        pos = pos % 31
        
        if list[z][pos] == "#":
            count += 1
    
    print("trees: ", count)
    return count


treeCount(filename, 3, 1)


"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

def countTotTrees(slopes):
    
    trees = 1
    for slope in slopes:
        trees *= treeCount(filename, slope[0], slope[1])

    print("tree dmg: ", trees)
    return trees
    
countTotTrees(slopes)
    

