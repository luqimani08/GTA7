import random


def innbrudd():
    print("Du går rundt og ser etter noe å gjøre! "
    "du ser et hus med en safe. Døre har en lås med 3 ulike tall. 1 2 og 3. Velger du feil, sendes en alarm til politiet!" \
    "Tar du sjansen, eller drar du vekk?")
    riktig = random.randint ( 1, 3 )
    

    valg = input("hvilken velger du? 1, 2, eller 3?")


    if valg != "1" and valg != "2" and valg != "3":

        print("Feil! politet kom!")
        return True

    if int(valg) == riktig:
        print("Døren åpnet!")
        print("Du gikk inn i huset og ser 300$")
        return True
    else:
        print("Alarmen går!")
        return False

if not innbrudd():
    exit()