def verschluesselterText(klartext, schluessel):
    geheimtext = ''
    for zeichen in klartext:
        zahl = ord(zeichen)
        neuezahl = zahl + schluessel
        if neuezahl > 90 and neuezahl < 90 + schluessel + 1 or neuezahl > 122:  #90 = ord('Z')
            neuezahl = neuezahl - 26
        neueszeichen = chr(neuezahl)
        geheimtext = geheimtext + neueszeichen
    return geheimtext

def entschluesselterText(geheimtext, schluessel):
    klartext = ''
    for zeichen in geheimtext:
        zahl = ord(zeichen)
        neuezahl = zahl - schluessel
        if neuezahl < 65 or neuezahl < 97 and neuezahl > 97 - schluessel - 1:  #65 = ord('A'), 97 = ord('a')
            neuezahl = neuezahl + 26
        neueszeichen = chr(neuezahl)
        klartext = klartext + neueszeichen
    return klartext

t = str(input('Bitte gib den zu verschlüsselnden Text ein -> '))
s = int(input('Bitte gib den Verschiebungsschlüssel ein: -> '))
geheimtext = verschluesselterText(t, s)
print("Der entschlüsselte Text lautet:", entschluesselterText(geheimtext, s))
print("Der verschlüsselte Text lautet:", verschluesselterText(t, s))
