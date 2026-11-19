class Character:
    def __init__(self, navn: str, alder: int, høyde: int, hudfarge: str):
        self.navn = navn
        self.alder = alder
        self.høyde = høyde
        self.hudfarge = hudfarge   
        self.liv = 100
        self.penger = 2000


navn = input("Navn: ")
alder = int(input("Alder: "))
høyde = int(input("Høyde: "))
hudfarge = input("Hudfarge: ")

spiller = Character(navn, alder, høyde, hudfarge)

print(navn)
print(alder)
print(høyde)
print(hudfarge)
