import random

def Encounter():
    liste = ["Junaid", "Zakariya", "Ashwin", "Amir", "Martin", "Abod", "Luqman", "Laith"]
    index = random.randint(0, len(liste)-1)
    navn = liste[index]

    print("Du gårnedover gata når en person kommer bort til deg.")
    print(navn + ': "Ey, hva glor du på? Tror du at du eier gata?"')

    print("1. Ignorer ham")
    print("2. Svar med insults")
    print("3. Angrip ham")

    valg = input("Hva velger du? ")

    if valg == "1":
        print("Du ignorerer " + navn + " og går videre.")
        print(navn + ': "ja, bare gå videre din tulling."')
        return True

    elif valg == "2":
        print("Du svarer tilbake med noen rasistiske kommentarer.")
        print(navn + ': "Hva sa du til meg?!"')
        print("Han blir sint og begynner å rope etter deg.")
        print("Du går videre mens han fortsetter å snakke.")

        return True

    elif valg == "3":
        print("Du angriper " + navn + "!")
        print("En person i nærheten ringer politiet.")
        print("Politiet ankommer, Løp.")
        print("Du har nå 2 stjerner i wanted level.")

        return False

    else:
        print("hvorfor er du vanskelig? bare velg.")
        return True

Encounter()