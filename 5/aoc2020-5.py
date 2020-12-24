# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:15:45 2020

@author: eateren
"""

import math


def seatReader(filename):
    
    with open(filename) as file:
        list = file.readlines()
        
    list = [line.strip() for line in list]
    print(list)
    
    seatIDS = []
    
    for item in list:
        
        rowLower = 0
        rowUpper = 127
        
        for x in item[:7]:
            if x == "F":
                rowUpper = rowUpper - math.ceil((rowUpper - rowLower)/2)
            elif x == "B":
                rowLower = rowLower + math.ceil((rowUpper - rowLower)/2)
                
            print(item, rowLower)
        

        
        colLower = 0
        colUpper = 7
        for x in item[7:]:
            if x == "L":
                colUpper = colUpper - math.ceil((colUpper - colLower)/2)
            elif x == "R":
                colLower = colLower + math.ceil((colUpper - colLower)/2)
                
            print(item, colLower)
                
        seatID = rowLower * 8 + colLower
        print(seatID)
        
        seatIDS.append(seatID)
        
    return seatIDS
        

def findSeat(seatIDS):
    for x in range(0,len(seatIDS)):
        try:
            if seatIDS[x] - seatIDS[x+1] == -2:
                print(seatIDS[x], seatIDS[x+1])
                
        except:
            pass
    
                