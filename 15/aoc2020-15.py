# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:02:46 2020

@author: eateren
"""

data = [0,6,1,7,2,19,20] #0, 7, 
tdata = [0,3,6] #0, 3

# create dict
def playGame(data, turns):
    
    dictNums = {num:index for index, num in enumerate(data, start=1)}
    
    newNum = 0  
    lastNum = 0
    for x in range(len(data) + 1, turns + 1):
        
        if newNum in dictNums.keys():
            nextNum = x - dictNums[newNum]
            dictNums[newNum] = x
            lastNum = newNum
            newNum = nextNum
        else:
            dictNums[newNum] = x
            lastNum = newNum
            newNum = 0

    print(x, lastNum)
    
playGame(data, 2020)
playGame(data, 30000000)