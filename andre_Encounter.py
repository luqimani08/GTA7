from character import spiller
def slasskamp(character):
    print("Du går rundt i Grorud og møter noen som lager bråk")
    print("Du drar til personen og ber han være stille, men han begynner å skrike på deg")
    print("velger du å slå til han og ta risken, eller går du vekk?")
    valg = input("Vil du slå han, eller gå vekk? ")

    if valg == "slå han":
        print("Du slo han hardt!")
        character.liv -= 10
        print("han slo hardt tilbake og du mista 10 liv!", character.liv)
    else:
        print("du gikk videre med dagen din")

slasskamp(spiller)