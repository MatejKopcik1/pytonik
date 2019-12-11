import tkinter
from random import randrange, randint

sirka = 1600
vyska = 900
c=tkinter.Canvas(width=sirka, height=vyska, bg="white")
c.pack()

x, y = sirka/2, vyska/2
for _ in range(201):
    a = randrange(1601)
    b = randrange(901)
    if a < 800 and b < 450:
        farba = "blue"
    elif a > 800 and b < 450:
        farba = "red"
    elif a < 800 and b > 450:
        farba = "green"
    elif a > 800 and b > 450:
        farba = "yellow"

    c.create_line(x,y,a,b,fill=farba, width = 3)

c.create_text(x,y,text = "MOZAX", font = "Times 120 bold", fill = "black", activefill = "purple")
