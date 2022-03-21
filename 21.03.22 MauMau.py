import random


def stapel_zeigen(stapel):
    for i in range(0, len(stapel)):
        print(i)
# gib alle karten eines stapels mit name und index aus


def stapel_erstellen():
    stapel = []
    for i in range(1, 33):
        stapel.append(i)
    return stapel
# verschiebt karte von stapel1 zu stapel2 (zB Hand => Ablage)


def karte_verschieben(stapel1, stapel2, kartenZahl):
    stapel2.append(stapel1[kartenZahl])
    del stapel1[kartenZahl]
# kreiert den start-stapel und returnt ihn


def ganze_hand_ziehen(stapel, hand):
    if len(stapel) > 0:
        for i in range(0, 7):
            karte_verschieben(stapel, hand, random.randint(0, len(stapel)-1))
    else:
        print("Der Stapel ist leer!")
# zieht 7 karten von kartenstapel auf hand


def hand_auswählen(hand, ablage):
    print("")
    print("Ihre Hand hat die Karten: ")
    stapel_zeigen(hand)
    gewählte_zahl = int(input(
        "Bitte geben sie den Index einer Karte ihrer Hand ein: "))
    return gewählte_zahl
# gibt hand aus und fragt nach input zum kartenlegen


def karte_legen(hand, ablage):
    gewählte_zahl = hand_auswählen(hand, ablage)
    while not gewählte_zahl < len(hand):
        print(gewählte_zahl, " ist nicht auf ihrer Hand")
        gewählte_zahl = hand_auswählen(hand, ablage)
    karte_verschieben(hand, ablage, gewählte_zahl)
# legt karte wenn diese auf der hand ist


kartenstapel = stapel_erstellen()
kartenhand = []
ablagestapel = []

karte_verschieben(kartenstapel, ablagestapel,
                  random.randint(0, (len(kartenstapel)-1)))
ganze_hand_ziehen(kartenstapel, kartenhand)
karte_legen(kartenhand, ablagestapel)

print("")
print("Kartenstapel:")
stapel_zeigen(kartenstapel)
print("")
print("Kartenhand:")
stapel_zeigen(kartenhand)
print("")
print("Ablagestapel:")
stapel_zeigen(ablagestapel)
# print zur überprüfung
