a = int(input("a = "))

if a - int(a/3)*3 == 0 :
    print("Číslo ", a, "je deliteľné tromi")
else:
    print("Číslo ", a, "nie je deliteľné tromi")

if a - int(a/2)*2 == 0 :
    print("Číslo ", a, "je párne")
else:
    print("Číslo ", a, "nie je párne")
