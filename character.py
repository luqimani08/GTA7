class Character:
    def __init__(self, navn: str, alder: int, høyde: int, hudfarge: str):
        self.navn = navn
        self.alder = alder
        self.høyde = høyde
        self.hudfarge = hudfarge   # denne linjen manglet også
        self.liv = 100
        self.penger = 2000


navn = input("Navn: ")
alder = int(input("Alder: "))
høyde = int(input("Høyde: "))
hudfarge = input("Hudfarge: ")

spiller = Character(navn, alder, høyde, hudfarge)

print(spiller.navn)
print(spiller.alder)
print(spiller.høyde)
print(spiller.hudfarge)
