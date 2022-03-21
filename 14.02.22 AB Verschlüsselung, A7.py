# eingabe des zu versschlüsselnden Textes
klartext = str(input('Gib ein Wort ein:'))
# definieren der variable geheimtext
geheimtext = ''
# schleife für string klartext
for zeichen in klartext:
    # ascii zahlencode abspeichern
    zahl = ord(zeichen)
    # ascii des neuen buchstabens
    neuezahl = zahl + 3
    # wenn neue zahl über Z ist
    if neuezahl > 90:
        # anderes ende des Alphabets
        neuezahl = neuezahl - 26
    # ascii zu buchstabe
    neueszeichen = chr(neuezahl)
    # geheimtext erweitern mit verschlüsseltem buchstaben
    geheimtext = geheimtext + neueszeichen
# ausgabe des endtextes
print(geheimtext)