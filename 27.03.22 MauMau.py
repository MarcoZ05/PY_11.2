import random

cardSymbolSwitch = {
    0: "Herz",
    1: "Kreuz",
    2: "Karo",
    3: "Pick",
}

cardValueSwitch = {
    1: "7",
    2: "8",
    3: "9",
    4: "10",
    5: "Bube",
    6: "Dame",
    7: "Koenig",
    8: "Ass",
}


def getCardSymbol(card):
    return int(card) % 4


def getCardValue(card):
    return int((card+(4-getCardSymbol(card)))/4)


def deckName(card):
    cardSymbol = getCardSymbol(card)
    cardValue = getCardValue(card)
    karten_name = str(cardSymbolSwitch.get(cardSymbol)) + \
        " " + str(cardValueSwitch.get(cardValue))
    return karten_name


def createDeck():
    deck = []
    for i in range(1, 33):
        deck.append(i)
    return deck


def moveRandomCard(deck1, amount):
    deck2 = []
    for i in range(0, amount):
        randomNum = random.randint(0, len(deck1)-1)
        deck2.append(deck1[randomNum])
        del deck1[randomNum]
    return deck2


def moveSelectedCard(deck1, deck2, index):
    deck2.append(deck1[index])
    del deck1[index]


def printDeck(deck):
    for i in range(0, len(deck)):
        print(f"{deckName(deck[i])} => {(i+1)}")


def playCard(thisHand, discDeck):
    print("")
    print("Deine Karten:")
    printDeck(thisHand)
    print("")
    print("Ablagestapel: "+deckName(discDeck[-1]))

    cardIndex = int(input("Gebe einen Kartenindex ein: "))-1

    if cardIndex < 0 or cardIndex >= len(thisHand):
        print("")
        print("")
        print(f"Ungueltige Eingabe: {(cardIndex+1)}")
        playCard(thisHand, discDeck)
        return
    elif getCardSymbol(thisHand[cardIndex]) != getCardSymbol(discDeck[-1]) and getCardValue(thisHand[cardIndex]) != getCardValue(discDeck[-1]):
        print("")
        print("")
        print(f"Diese Karte passt nicht: {(cardIndex+1)}")
        playCard(thisHand, discDeck)
        return

    moveSelectedCard(thisHand, discDeck, cardIndex)
    print("")


def game(playerAmount):
    # stop game if playerAmount is not valid
    if(playerAmount > 3):
        print("Das Maximum der Spieler ist 3!")
        return
    if(playerAmount < 2):
        print("Das Minimum der Spieler ist 2!")
        return

    # creates all decks
    mainDeck = createDeck()
    handDecks = []
    for i in range(0, playerAmount):
        handDecks.append(moveRandomCard(mainDeck, 7))
    discDeck = moveRandomCard(mainDeck, 1)

    # game loop
    player = 0
    while len(handDecks[player]) != 0:
        thisHand = handDecks[player]
        print("Player {(player+1)}")
        playCard(thisHand, discDeck)

        if player == playerAmount-1:
            player = 0
        else:
            player += 1

    print(f"Spieler {(player+1)} hat gewonnen.")
    print("Uebrige Karten:")
    for i in range(0, playerAmount):
        printDeck(handDecks[player])


game(3)
