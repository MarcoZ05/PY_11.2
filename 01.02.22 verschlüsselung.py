# splitting the input string into an array
encrypted = list(str(input("Nachricht: ")))
# key input
key = int(input("Verschlüsselung(-26 bis 26): "))

# function for de-/encrypting letters
def decrLetter(letter):
    if ord(letter) <= 90 and ord(letter) >= 65:
        if ord(letter)+key > 90:
            # if new letter over Z, start counting under/at A
            return chr(ord(letter)+key-26)
        elif ord(letter)+key < 65:
            # if new letter under A, start counting over/at Z
            return chr(ord(letter)+key+26)
        else:
            # normal de-/encrypting
            return chr(ord(letter)+key)
    elif ord(letter) <= 122 and ord(letter) >= 97:
        if ord(letter)+key > 122:
            # if new letter over Z, start counting under/at A
            return chr(ord(letter)+key-26)
        elif ord(letter)+key < 97:
            # if new letter under A, start counting over/at Z
            return chr(ord(letter)+key+26)
        else:
            # normal de-/encrypting
            return chr(ord(letter)+key)
    else:
        # return the symbol
        return letter

# putting de-/encrypted letters together
def decrAll(arr):
    i = 0
    string = ""

    while i != len(arr):
        string += decrLetter(arr[i])
        i+=1
    return string

print(decrAll(encrypted))