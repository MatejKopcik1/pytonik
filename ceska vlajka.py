import tkinter
from random import randrange

sirka = 1200
vyska = 800

c = tkinter.Canvas(width = sirka, height = vyska)
c.pack()

for _ in range(6000):
    x = randrange(10, sirka - 10)
    y = randrange(10, vyska - 10)
    if y >= x and y <= 400:
        farba = "blue"
    elif x <= -y+vyska and y > vyska/2:
        farba = "blue"
    elif y > vyska / 2:
        farba = "red"
    else:
        farba = "white"

    c.create_rectangle(x-10, y-10, x+10, y+10, fill = farba)
