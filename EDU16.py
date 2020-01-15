h = float(input("Hmotnosť človeka v kg: "))
v = float(input("Výška človeka v cm: "))/100.0

bmi = float(h/v**2)

if bmi < 18.5:
    print(bmi)
    print("BMI < 18.5 => podváha")
elif 18.5 <= bmi < 25:
    print(bmi)
    print("18.5 <= BMI < 25 => normálna hmotnosť")
elif 25 <= bmi < 30:
    print(bmi)
    print("25 <= BMI < 30 => nadváha")
elif 30 < bmi:
    print(bmi)
    print("30 < bmi => obezita")

