import numpy as np, random

def savecards(cards, filelocation = r""):
    try:
        np.save(filelocation, cards)
    except:
        print("error: cannot save cards")
    return cards


def readcards(filelocation = r""):
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
