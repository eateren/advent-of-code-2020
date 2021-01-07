# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:42:49 2020

@author: eateren
"""

filename = "data.txt"

def readData(filename):
    
    with open(filename) as file:
        data = file.read().replace("\n", " ").split("  ")
        
    return data

data = readData(filename)

def parseData(data):
    
    parsedData = []
    for x in data:
        if "byr" in x and "iyr" in x and "eyr" in x and "hgt" in x and "hcl" in x and "ecl" in x and "pid" in x:
            parsedData.append(x.split())
            
    return parsedData


parsedData = parseData(data)


def cleanData(parsedData):
    
    cleanedData = [ ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]  ]
    
    for line in parsedData:
        
        cleanedLine = []
        for i in range(0,8):
            
            for item in line:
                if cleanedData[0][i] in item:
                    cleanedLine.append(item[4:])
                    
        cleanedData.append(cleanedLine)
                
            
    return cleanedData
            
cleanedData = cleanData(parsedData)
print(len(cleanedData))


def checkCleandedData(cleanedData):

    
    count = 0
    for lineno, line in enumerate(cleanedData):
        
        if lineno == 0:
            continue
        
        chk = 0
        for no, item in enumerate(line):
            
            if no == 0:
                try:
                    if int(item) >= 1920 and int(item) <= 2002:
                        chk += 1
                except:
                    pass
            
            if no == 1:
                try:
                    if int(item) >= 2010 and int(item) <= 2020:
                        chk += 1
                except:
                    pass
            
            if no == 2:
                try:
                    if int(item) >= 2020 and int(item) <= 2030:
                        chk += 1
                except:
                    pass
        
            if no == 3:
                try:
                    if "cm" in item:
                        h = int(item.replace("cm",""))
                        if h >= 150 and h <= 193:
                            chk += 1
                            
                    elif "in" in item:
                        h = int(item.replace("in",""))
                        if h >= 59 and h <= 76:
                            chk += 1                            
                except:
                    pass
                
            if no == 4:
                try:
                    if item[0] == "#" and len(item) == 7:
                        charChk = 0
                        for x in item:
                            if x in "0123456789abcdef":
                                charChk += 1
                        if charChk == 6:
                            chk += 1
                            
                except:
                    pass
            
            if no == 5:
                try:
                    if item in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        chk += 1
                        
                except:
                    pass
            
            if no == 6:
                try:
                    charChk = 0
                    for x in item:
                        if x in "0123456789":
                            charChk += 1
                    
                    if charChk == 9:
                        chk +=1
                        
                except:
                    pass
        
        if chk == 7:
            count += 1
    
    print(count)
    return count
            
checkCleandedData(cleanedData)        
        
    