zootiere = ["Elefant", "Giraffe", "Tiger", "Gepard"]

def reset():
    zootiere = ["Elefant", "Giraffe", "Tiger", "Gepard"]

def aufgC():
    print(zootiere[0],zootiere[2])
    print(zootiere[1],zootiere[3])

def aufgD():
    zootiere[2] = "Löwe"
    print(zootiere[2])

def aufgE():
    zootiere.append("Stachelschwein")
    zootiere.append("Kuh")
    zootiere.append("Hund")
    print(zootiere)

def aufgF():
    print(len(zootiere))

def aufgG():
    print(zootiere[0:3])    # gibt ersten 3 aus


def aufgH():
    print(zootiere[2:]) # gibt 3.stelle plus nachfolgende aus
    print(zootiere[:2]) # gibt alles vor 3.stelle aus
