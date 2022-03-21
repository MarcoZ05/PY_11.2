import random

# switch objekt um von symbol index zu symbol name zu kommen
switch_karten_symbol = {
    0:"Herz",
    1:"Kreuz",
    2:"Pick",
    3:"Karo",
}

# switch objekt um von wert index zu wert name zu kommen
switch_karten_wert = {
    1:"7",
    2:"8",
    3:"9",
    4:"10",
    5:"Bauer",
    6:"Dame",
    7:"Koenig",
    8:"Ass",
}

# wandelt karten index zu kartenname und returnt diesen
def karten_wertigkeit(karten_index):
    karten_symbol = karten_index % 4 
    karten_wert = int((karten_index+(4-karten_symbol))/4)
    karten_name = str(switch_karten_symbol.get(karten_symbol)) + " " + str(switch_karten_wert.get(karten_wert))
    return karten_name

# gib alle karten eines stapels mit name und index aus
def karten_zeigen(stapel):
    for i in range(0,len(stapel)):
        print(karten_wertigkeit(stapel[i])+" => "+str(stapel[i]))

# kreiert den start-stapel und returnt ihn
def stapel_erstellen():
    stapel = []
    for i in range(1,33):
        stapel.append(i)
    return stapel

# verschiebt karte von stapel1 zu stapel2 (zB Hand => Ablage)
def karte_verschieben(stapel1,stapel2):
    kartenZahl = random.randint(0,len(stapel1))
    stapel2.append(stapel1[kartenZahl])
    del stapel1[kartenZahl]

# zieht 7 karten von kartenstapel auf hand
def ganze_hand_ziehen(stapel,hand):
    for i in range(0,7):
        karte_verschieben(stapel, hand)

# gibt hand aus und fragt nach input zum kartenlegen
def hand_auswählen(hand):
    print("Ihre Hand hat die Karten: ")
    karten_zeigen(hand)
    gewählte_zahl = int(input("Bitte geben sie eine Zahl ihrer Hand ein: "))
    return gewählte_zahl

# legt karte wenn diese auf der hand ist
def karte_legen(hand,ablage):
    gewählte_zahl = hand_auswählen(hand)
    while not gewählte_zahl in hand:
        print(gewählte_zahl," ist nicht auf ihrer Hand")
        gewählte_zahl = hand_auswählen(hand)
    karte_verschieben(hand,ablage)
    

kartenstapel = stapel_erstellen()
kartenhand = []
ablagestapel = []

# beispielsweise einmal ganze hand ziehen und einmal legen
ganze_hand_ziehen(kartenstapel,kartenhand)
karte_legen(kartenhand,ablagestapel)
# print zur überprüfung
print("Kartenstapel: ",kartenstapel)
print("Kartenhand: ",kartenhand)
print("Ablagestapel: ",ablagestapel)

# Issue: & C:/Users/super/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/super/OneDrive/Desktop/Programmieren/PY_11.2/21.03.22 MauMau.py"
# Traceback (most recent call last):
#   File "c:\Users\super\OneDrive\Desktop\Programmieren\PY_11.2\21.03.22 MauMau.py", line 75, in <module>  
#     karte_legen(kartenhand,ablagestapel)
#   File "c:\Users\super\OneDrive\Desktop\Programmieren\PY_11.2\21.03.22 MauMau.py", line 62, in karte_legen
#     gewählte_zahl = hand_auswählen(hand)
#   File "c:\Users\super\OneDrive\Desktop\Programmieren\PY_11.2\21.03.22 MauMau.py", line 57, in hand_auswählen
#     gewählte_zahl = int(input("Bitte geben sie eine Zahl ihrer Hand ein: "))
# ValueError: invalid literal for int() with base 10: '& C:/Users/super/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/super/OneDrive/Desktop/Programmieren/PY_11.2/21.03.22 MauMau.py"'