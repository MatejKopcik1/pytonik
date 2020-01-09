print("Výpočet ceny jazdy zo spotreby auta a ceny benzínu")
spotreba = float(input("Spotreba: "))
cenazal = float(input("Cena benzínu za 1 liter: "))
draha = float(input("Vzdialenosť v kilometroch: "))

cena = spotreba * cenazal * draha / 100.0

print("Cena cesty v aute so spotrebou",spotreba,"litrov a cene paliva",cenazal,"€ za liter, bude",cena,"€")
