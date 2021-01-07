# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:37:23 2020

@author: eateren
"""
import re


datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.read()
        
    
    rulesData, msgData = data.split("\n\n")
    
    ruleDict = {}
    for line in rulesData.split("\n"):
        
        key = int(line.split(": ")[0])
        ruleList = [rules.split(" ") for rules in line.split(": ")[1].strip().split(" | ")]
        ruleDict[key] = ruleList
    
    ruleDict = dict(sorted(ruleDict.items(), key=lambda item: item[0]))
    
    
    messages = []
    for line in msgData.split("\n"):

        messages.append(line.strip())
    
    return ruleDict, messages


ruleDict, message = readData(datafile)




# used William Y. Fengs help again at https://www.youtube.com/watch?v=hKg5z_EPbhs&t=818s
# this code is rewrites many of his steps

# database of rule regexes
ruleList = {}


# functions that translate to regex

#@lru_cache(None)
# not using the lru_cache because I built the data as lists before looking up
# this method
def transfRegex(rule):
    
    char = ""
    if '"' in rule[0][0]:
        
        char += rule[0][0][1]
        
    else:
        
        for ruleset in rule:

            regex = "(" + ")(".join([getSubRule(int(i)) for i in ruleset]) + ")|"
            char += regex
        
        char = char[:-1]
        if len(rule) == 2:
            char = "(" + char + ")"
        
    return char



def getSubRule(ruleNo):
    
    if ruleNo in ruleList:
        
        return ruleList[ruleNo]
    
    else:
        
        char = transfRegex(ruleDict[ruleNo])
        ruleList[ruleNo] = char
        
        return char


regex0 = getSubRule(0)


def countMsg(regex0, message):
    
    count = 0
    for msg in message:
        
        matches = bool(re.fullmatch(regex0, msg))
        count += matches

    return count


print(countMsg(regex0, message))


"""
PART TWO
using Mr. Fengs solution we add the following:
"""


# database of rule regexes
ruleList2 = {}


# functions that translate to regex

#@lru_cache(None)
def transfRegex2(rule):
    
    char = ""
    if '"' in rule[0][0]:
        
        char += rule[0][0][1]
        
    else:
        for ruleset in rule:

            regex = "(" + ")(".join([getSubRule2(int(i)) for i in ruleset]) + ")|"
            char += regex
        
        char = char[:-1]
        if len(rule) == 2:
            char = "(" + char + ")"
        
    
    return char



def getSubRule2(ruleNo):
    
    if ruleNo == 8:
        
        return rule8
    
    elif ruleNo == 11:
        
        return rule11
    
    else:
        
        char = transfRegex2(ruleDict[ruleNo])
        ruleList2[ruleNo] = char
        
        return char


# so pretty much rule 8 is now either rule 42 or rule 42 as many times as it
# wants.  So we add a "+" to the regex that matches one or more occurences
rule42 = getSubRule2(42)
rule31 = getSubRule2(31)

rule8 = f"({rule42})+"

# and rule 11 is simliar in that it is as many occurences of rule 42 on the
# left and rule 31 on the right in equal amounts
rule11List = []
for x in range(1,30):
    rule11List.append(f"({rule42}){{{x}}}({rule31}){{{x}}}")

rule11 = "(" + ")|(".join([subrule for subrule in rule11List]) + ")"


regex0Two = getSubRule2(0)


def countMsg2(regex0Two, message):
    
    count = 0
    for msg in message:
        
        matches = bool(re.fullmatch(regex0Two, msg))
        count += matches

    return count

print(countMsg2(regex0Two, message))