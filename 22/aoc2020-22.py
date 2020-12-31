# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:08:29 2020

@author: eateren
"""

datafile = "data.txt"

def readData(datafile):
    
    with open(datafile) as file:
        data = file.read()
        
    data = data.split("\n\n")
    deck1 = list(map(int, data[0].split("\n")[1:]))
    deck2 = list(map(int, data[1].split("\n")[1:]))
    
    return deck1, deck2

deck1, deck2 = readData(datafile)



def gameRound(deck1, deck2):
    
    d1, d2 = deck1[0], deck2[0]
    
    if d1 > d2:
        deck1.remove(d1)
        deck2.remove(d2)
        deck1 += [d1, d2]
    else:
        deck2.remove(d2)
        deck1.remove(d1)
        deck2 += [d2, d1]


def playUntilWin(deck1, deck2):
    
    while len(deck1) > 0 and len(deck2) > 0:
        
        gameRound(deck1, deck2)
        
    return deck1, deck2


def computeScore(deck1, deck2):
    
    playUntilWin(deck1, deck2)
    
    if len(deck1) > 0:
        deck = deck1.copy()
    else:
        deck = deck2.copy()
        
    deck.reverse()
    
    score = 0
    for no, card in enumerate(deck):
        score += (no + 1) * card
    
    print(score)
    return score
    
    
computeScore(deck1, deck2)
    
    
    
# part two, reset decks
# part two modeled after https://github.com/r0f1/adventofcode2020/blob/master/day22/main.py#L29
# learned that lists get affected by recursed function... used sets instead.


deck1, deck2 = readData(datafile)


def recurrGame(deck1, deck2):
    
    prevDecks1 = set()
    prevDecks2 = set()

    while len(deck1) > 0 and len(deck2) > 0:
        strDeck1 = ",".join(list(map(str, deck1)))
        strDeck2 = ",".join(list(map(str, deck2)))
        if (strDeck1 in prevDecks1) or (strDeck2 in prevDecks2):
            return "1", deck1
        
        prevDecks1.add(strDeck1)
        prevDecks2.add(strDeck2)
        
        d1 = deck1.pop(0)
        d2 = deck2.pop(0)
        if d1 <= len(deck1) and d2 <= len(deck2):
            subDeck1 = deck1.copy()
            subDeck2 = deck2.copy()
            winningDeck = recurrGame(subDeck1[:d1], subDeck2[:d2])[0]
        else:
            if d1 > d2:
                winningDeck = "1"
            else:
                winningDeck = "2"
        
        if winningDeck == "1":
            deck1 += [d1, d2]
        else:
            deck2 += [d2, d1]
        
    if len(deck2) == 0:
        return "1", deck1
    else:
        return "2", deck2


winningDeck = recurrGame(deck1, deck2)[1]


def computeScore2(winningDeck):
    
    winningDeck.reverse()
    
    score = 0
    for no, card in enumerate(winningDeck):
        score += (no + 1) * card
    
    print(score)
    return score
    