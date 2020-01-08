print("Výpočet objemu a povrchu kvádru z jeho strán a,b,c v cm kubických")
ax = input("a = ")
bx = input("b = ")
cx = input("c = ")

a = float(ax)
b = float(bx)
c = float(cx)

s = float(2*a*b+2*a*c+2*b*c)
V = float(a*b*c)

print("Objem kvádra je", V, "cm kubických a jeho povrch je", s, "cm štvorcových")
