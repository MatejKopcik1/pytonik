print("Prima Banka Šurany")
vklad = float(input("Výška vkladu:"))
m = float(input("Ročná úroková miera v %:"))
koniec = (100.0 + m) * vklad / 100

print("Suma na konci roka pri úrokovej miere", m, "a vklade", vklad, "bude", koniec,"€")
