from email.policy import default
import random


def createDeck():
    deck = []

    for symbol in ["Herz", "Kreuz", "Pick", "Karo"]:
        for value in [7, 8, 9, 10, "Bube", "Dame", "Koenig"]:
            deck.append([value, symbol])

    return deck


def getHand(deck, amount):
    hand = []

    for i in range(0, amount):
        rand = random.randint(0, len(deck)-1)
        hand.append(deck[rand])
        del deck[rand]

    return hand


def sortDeck(hand):
    # erstellt ein standart-deck
    mainDeck = createDeck()
    # erstellt das rueckgabe-deck
    returnDeck = []

    # erstellt 2 indixes
    mainIndex = 0
    handIndex = 0

    # solange
    while len(returnDeck) != len(hand):

        if mainDeck[mainIndex] == hand[handIndex]:
            returnDeck.append(hand[handIndex])

        if handIndex+1 == len(hand):
            handIndex = 0
            mainIndex += 1
        else:
            handIndex += 1

    return returnDeck


mainDeck = createDeck()
handDeck = getHand(mainDeck, 7)

print(handDeck)


print("")
print(sortDeck(handDeck))
