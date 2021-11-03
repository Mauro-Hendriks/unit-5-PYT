
verzekering_per_maand = 23.0
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2

km_per_maand = "";





while not isinstance(km_per_maand, float):

      
    try:
        
        
        km_per_maand = input("hoe veel km rij je per maand: ")
        
        km_per_maand = float(km_per_maand)

        maandkosten = (km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand
        
        print("dit zijn je maandlijkse kosten:" + str(round(maandkosten, 2)))

    except ValueError:
        
        print(km_per_maand + " is geen geldig getal!")

      