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


kartenstapel = stapel_erstellen()
kartenhand = []
ablagestapel = []

karte_verschieben(kartenstapel, ablagestapel,
                  random.randint(0, (len(kartenstapel)-1)))
ganze_hand_ziehen(kartenstapel, kartenhand)

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
