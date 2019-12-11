import tkinter
from random import randrange, randint

sirka = 1200
vyska = 800
c=tkinter.Canvas(width=sirka, height=vyska, bg="white")
c.pack()



for _ in range(3000):
    x, y = randrange(10, sirka - 10), randrange(10, vyska - 10)
    if 300 < x < 400:
        farba = "white"
    elif 350 < y < 450:
        farba = "white"

    else:
        farba = "red"

    c.create_oval(x-20,y-20,x+20,y+20, fill = farba)

c.create_text(sirka/2, vyska/2, text="D E N M A R K", font = "times 100")
