import math
pi = math.pi
print("Výpočet obvodu kružnice, obsahu kruhu a objemu gule z veľkosti polomeru")
r = float(input("r = "))
s = float(pi * r * r)
o = float(2 * pi * r)
V = float(4/3 * pi * r * r * r)
print("Obsah kruhu je", s)
print("Obvod kružnice je", o)
print("Objem gule je", V)
