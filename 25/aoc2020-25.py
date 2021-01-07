# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:42:37 2020

@author: eateren
"""


divNo = 20201227

cardKey = 11349501
doorKey = 5107328


def findLoopSize(key, subjNo = 7):
    
    loop = 0
    currNo = 1
    
    while currNo != key:
        
        loop += 1
        currNo = (currNo * subjNo) % divNo
        
    return loop


cardLoop = findLoopSize(cardKey)


def findEncKey(loop, subjNo):
    
    currNo = 1
    for x in range(loop):
        
        currNo = (currNo * subjNo) % divNo
    
    return currNo


print(findEncKey(cardLoop, doorKey))
    
