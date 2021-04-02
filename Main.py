import random

def Main_Decision():
    
    deciReturn = random.randint(1,3)
    return deciReturn


def CharDecision():
    
    charRandom = random.randint(1,2)

    if charRandom == 1:
        charReturn = random.randint(65,90)
        return charReturn

    elif charRandom == 2:
        charReturn = random.randint(97,122)
        return charReturn

    else:
        print("Error 2: could not randomise CHAR")


def NumDecision():
    
    numReturn = random.randint(0,9)
    return numReturn

def SignDecision():

    signReturn = random.randint(35,38)
    return signReturn

print("\nPassword Generator\n")
print("How many characters? ", end="")
numCharacters = int(input())
print("\n")

for x in range(numCharacters):

    deciResult = Main_Decision()
    
    if deciResult == 1:
        print(chr(CharDecision()), end="")

    elif deciResult == 2:
        print(NumDecision(), end="")

    elif deciResult == 3:
        
        print(chr(SignDecision()), end="")
        
    else:
        print("Error 1: Main decision was not executed") 

print("\n")

