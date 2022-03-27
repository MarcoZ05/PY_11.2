import random
from tracemalloc import stop

switch_karten_symbol = {
    0: "Herz",
    1: "Kreuz",
    2: "Pick",
    3: "Karo",
}
# switch objekt um von symbol index zu symbol name zu kommen

switch_karten_wert = {
    1: "7",
    2: "8",
    3: "9",
    4: "10",
    5: "Bauer",
    6: "Dame",
    7: "Koenig",
    8: "Ass",
}
# switch objekt um von wert index zu wert name zu kommen


def karten_wertigkeit(karten_index):
    print("kindex "+str(karten_index))
    karten_symbol = int(karten_index) % 4
    karten_wert = int((karten_index+(4-karten_symbol))/4)
    karten_name = str(switch_karten_symbol.get(karten_symbol)) + \
        " " + str(switch_karten_wert.get(karten_wert))
    return karten_name
# wandelt karten index zu kartenname und returnt diesen


def stapel_zeigen(stapel):
    for i in range(0, len(stapel)-1):
        print(karten_wertigkeit(stapel[i]) + " => "+str(i+1))
# gib alle karten eines stapels mit name und index aus


def stapel_erstellen():
    stapel = []
    for i in range(1, 33):
        stapel.append(i)
    return stapel
# verschiebt karte von stapel1 zu stapel2 (zB Hand => Ablage)


def karte_verschieben(stapel1, stapel2, kartenIndex):
    if len(stapel1) > 1:
        stapel2.append(stapel1[kartenIndex])
        del stapel1[kartenIndex]
    else:
        stapel_aufstocken(stapel1, stapel2)
# kreiert den start-stapel und returnt ihn


def stapel_aufstocken(stapel, ablage):
    for i in range(1, len(ablage)):
        if len(ablage) > 1:
            karte_verschieben(ablage, stapel, i)


def ganze_hand_ziehen(stapel, hand, ablage):
    if len(stapel) > 7:
        for i in range(0, 7):
            karte_verschieben(stapel, hand, random.randint(0, len(stapel)-1))
    else:
        stapel_aufstocken(stapel, ablage)
# zieht 7 karten von kartenstapel auf hand


def gewonnen(hand_i):
    print(F"Spieler ", (hand_i+1), " hat gewonnen!")


def gewinn_pruefen(hand):
    for hand_i in range(0, len(hand)):
        if len(hand[hand_i]) > 0:
            return False
        else:
            gewonnen(hand_i)
            return True


def hand_auswaehlen(hand, ablage, spieler):
    print("Ihre Hand hat die Karten: ")
    print(hand[spieler])
    stapel_zeigen(hand[spieler])
    print("ablage: "+str(ablage[-1]))
    print("Der Ablagestapel hat die Karte: " +
          str(karten_wertigkeit(ablage[-1])))
    gewaehlte_zahl = int(input(
        "Bitte geben sie den Index einer Karte ihrer Hand ein: "))
    return gewaehlte_zahl
# gibt hand aus und fragt nach input zum kartenlegen


def pruefe_karten(karte1_index, karte2_index):
    karte1_symbol = karte1_index % 4
    karte1_wert = int((karte1_index+(4-karte1_symbol))/4)
    karte2_symbol = karte2_index % 4
    karte2_wert = int((karte2_index+(4-karte2_symbol))/4)
    if karte1_symbol == karte2_symbol or karte1_wert == karte2_wert:
        return True
    return False


def karte_legen(stapel, hand, ablage, spieler):
    gewaehlte_zahl = hand_auswaehlen(hand, ablage, spieler)
    while not gewaehlte_zahl < len(hand[spieler]) and not pruefe_karten(hand[spieler[gewaehlte_zahl]], ablage[-1]):
        print(gewaehlte_zahl,
              " ist nicht auf ihrer Hand oder Passt nicht auf die Karte!")
        hand_auswaehlen(hand, ablage, spieler)
    karte_verschieben(hand, ablage, gewaehlte_zahl)
# legt karte wenn diese auf der hand ist


def spiel_zug(stapel, hand, ablage, spieler):
    karte_legen(stapel, hand, ablage, spieler)

    if spieler >= 2:
        spieler = 0
    else:
        spieler += 1


def spiel(stapel, hand, ablage):
    karte_verschieben(stapel, ablage, random.randint(0, len(stapel)))

    hand1 = []
    ganze_hand_ziehen(stapel, hand1, ablage)
    hand2 = []
    ganze_hand_ziehen(stapel, hand2, ablage)
    hand3 = []
    ganze_hand_ziehen(stapel, hand3, ablage)

    hand = [hand1, hand2, hand3]
    # spieler 1, 2 und 3 karten austeilen
    spieler = 0
    spiel_liste = [stapel, hand, ablage, spieler]

    while gewinn_pruefen(hand) == False:
        spiel_zug(stapel, hand, ablage, spieler)
        print(hand)


kartenstapel = stapel_erstellen()
kartenhand = []
ablagestapel = []

spiel(kartenstapel, kartenhand, ablagestapel)
