# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:10:59 2020

@author: eateren
"""

def dataReader(filename):
    
    with open(filename) as file:
        list = file.readlines()
    

    list = [line.strip().split(" ") for line in list]
    
    for line in list:
        line[1] = int(line[1])

    return list


data = dataReader("data.txt")


def runInstructions(data):
    
    ranLines = []
    step = 0
    acc = 0
    
    while step not in ranLines and step != 641:
        
        print("step", step)
        ranLines.append(step)
        
        if data[step][0] == "nop":
            step += 1

        elif data[step][0] == "jmp":
            step += data[step][1]
        
        elif data[step][0] == "acc":
            acc += data[step][1]
            step += 1
            print("acc", acc)
            print("step", step)
            
        
        
        print(ranLines)
        
    return [step, acc]


def dataStepAppender(data):
    

    for no, line in enumerate(data):
        if line[0] == "nop":
            line.append(1)
            line.append(no + 1)

        elif line[0] == "jmp":
            line.append(line[1])
            line.append(no + line[1])
        
        elif line[0] == "acc":
            line.append(1)
            line.append(no + 1)

    return data

newData = dataStepAppender(data)

def dataStepAppender2(newData):
    

    for no, line in enumerate(newData):
        if line[0] == "nop":
            line.append(no + line[1])

        elif line[0] == "jmp":
            line.append(no + line[1])
        
        elif line[0] == "acc":
            line.append(no + 1)

    return newData

newData2 = dataStepAppender2(newData)

# no bueno
def findStoppage(data):
    
    step = len(data) - 1
    
    #create idex
    index = []
    for line in data:
        index.append(line[5])
    
    while True:
        
           
        try:
            step = index.index(step)
            print(step)
        except:
            break


def bruteForceFinder(data):
    
    testData = newData2
    changeData = []
    
    
    for no, line in enumerate(data):
        
        if line[0] == "nop":
            
            testData[no][0] = "jmp"
            
            try:
                changeData.append(runInstructions(testData))
            except:
                print(no)
                break
            
            testData[no][0] = "nop"
            
            
        elif line[0] == "jmp":
            
            testData[no][0] = "nop"
            
            try:
                changeData.append(runInstructions(testData))
            except:
                print(no)
                break
            
            testData[no][0] = "jmp"
            
        else:
            
            try:
                changeData.append(runInstructions(testData))
            except:
                print(no)
                break
            
    

    
    
        

