import random

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
    karten_symbol = karten_index % 4
    karten_wert = int((karten_index+(4-karten_symbol))/4)
    karten_name = str(switch_karten_symbol.get(karten_symbol)) + \
        " " + str(switch_karten_wert.get(karten_wert))
    return karten_name
# wandelt karten index zu kartenname und returnt diesen


def stapel_zeigen(stapel):
    for i in range(0, len(stapel)):
        print(karten_wertigkeit(stapel[i])+" => "+str(i))
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
    print("Der Ablagestapel hat die Karte: " +
          str(karten_wertigkeit(ablage[-1])))
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
while len(kartenhand) != 0:
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
