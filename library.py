import numpy as np, random

def newcard(cards, word, meaning, example, prorate = 0):
    try:
        cards[word] = [meaning, example, prorate, prorate]
    except:
        print("error: cannot add new card")

def savecards(cards, filelocation = r"C:/users/limue/desktop/My Flashcard/words.npy"):
    try:
        np.save(filelocation, cards)
    except:
        print("error: cannot save cards")
    return cards


def readcards(filelocation = r"C:/users/limue/desktop/My Flashcard/words.npy"):
    try:
        cards = np.load(filelocation, allow_pickle='TRUE').item()
    except:
        print("error: cannot read cards")
    return cards

def getcard(card):
    try:
        return (random.choice(list(card.key())), random.choice(list(card.value())))
    except:
        print("error: cannot get card")

def clearcards(cards = {}):
    try:
        savecards(cards)
    except:
        print("error: cannot clear card")
    return cards

def erasecard(cards, d_key):
    try:
        cards.pop(d_key)
    except:
        print("connot erase card")
    return cards

def searchcard(cards, key):
    try:
        print("the meaning of \"" + key + "\" is \"" + cards[key][0] + "\"\nexample: " + cards[key][1])
    except:
        print("error: cannot find the card")

def reset_prorate(cards):
    try:
        for c in cards:
            cards[c][2] = 0
            cards[c][3] = 0
    except:
        print("cannot reset prorate")

def viewprorate(cards, key):
    return cards[key][2]

def calprorate(cards, key):
    try:
        if cards[key][2] == 0:
            cards[key][3] += 1
            cards[key][2] = cards[key][3]
        else:
            cards[key][2] -= 1
    except:
        print("cannot calculate prorate")
    
