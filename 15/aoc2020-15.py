# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:02:46 2020

@author: eateren
"""

# looked at someones solution and saw that a dictionary list is much faster

data = [0,6,1,7,2,19,20] #0, 7, 
tdata = [0,3,6] #0, 3

# create dict


dictNums = {num:index for index, num in enumerate(data, start=1)}
newNum = 0  

for x in range(len(data) + 1, 30000000 + 1):
    
    
    
    if newNum in dictNums.keys():
        nextNum = x - dictNums[newNum]
        dictNums[newNum] = x
        newNum = nextNum
    else:
        dictNums[newNum] = x
        newNum = 0

print(x, newNum)