invoer = "";

# Zolang de invoer geen float is, wordt deze while loop uitgevoerd
while not isinstance(invoer, float):
    verzekering_per_maand = 23
    benzine_kosten_per_liter = 1.54
    liter_per_kilometer = 0.2 

    try:
        km_per_maand = input("Hoeveel KM per maand rij je: ")
        
        invoer = float(invoer)

        print(str(maandkosten))

    except ValueError:
        print(invoer + " is geen geldig getal!")

    maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand  