def einzelAugabe(zeichenkette):
    for i in range(0, len(zeichenkette)):
        print(zeichenkette[i])

def vokale(zeichenkette):
    for i in range(0, len(zeichenkette)):
        if zeichenkette[i] == "A" or zeichenkette[i] == "E" or zeichenkette[i] == "I" or zeichenkette[i] == "O" or zeichenkette[i] == "U":
            print(zeichenkette[i])

def verdopplung(zeichenkette):
    output = ""
    for i in range(0, len(zeichenkette)):
        output += zeichenkette[i] + zeichenkette[i]
    print(output)

def umdrehen(zeichenkette):
    output = ""
    for i in range(1, len(zeichenkette)+1):
        output += zeichenkette[len(zeichenkette)-i]
    print(output)

def bereinigung(zeichenkette):
    for i in len(zeichenkette):
        print(zeichenkette[i].upper())
bereinigung("Hi")