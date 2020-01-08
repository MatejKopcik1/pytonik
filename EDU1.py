print("Celočíslený podiel a zvyšok po delení dvoch čísel")
px = input("Napíš prvé číslo:")
dx = input("Napíš druhé číslo:")
p = float(px)
d = float(dx)
podiel = int(p / d)

z = float(p - podiel * d)


print("Celočíselný podiel je ", podiel, ",zvyšok je ", z)
