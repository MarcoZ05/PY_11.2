import random

def compareLottoNum(input,set):
    rightNumberCounter = 0
    for i in range(0,6):
        if input[i] in set:
            rightNumberCounter += 1
    return rightNumberCounter

def inputLottoNum():
    inputNumList = []
    while len(inputNumList) != 6:
        inputNum = int(input("Eingabe der "+str(len(inputNumList)+1)+". Lottozahl: "))
        if inputNum not in inputNumList and 50 > inputNum and inputNum > 0:
            inputNumList.append(inputNum)
        else:
            print("Invalid number "+str(inputNum))
    inputNumList.sort()
    return inputNumList

def randLottoNum():
    lottoNumList = [random.randint(1,49)]
    while len(lottoNumList) != 6:
        randNum = random.randint(1,49)
        if randNum not in lottoNumList:
            lottoNumList.append(randNum)
    lottoNumList.sort()
    return lottoNumList

def lotto():
    inputNumList = inputLottoNum()
    randNumList = randLottoNum()
    print()
    print(F"You numbers are: ",inputNumList)
    print(F"The right numbers are: ",randNumList)
    print(F"You got ",compareLottoNum(inputNumList,randNumList)," right!")

lotto()
