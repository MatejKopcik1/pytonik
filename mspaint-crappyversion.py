import tkinter
from random import randrange

vyska = 1600
sirka = 900

c = tkinter.Canvas(width = sirka, height = vyska, bg = "white")
c.pack()

def pohyb(event):
    x, y = event.x, event.y
    r = 5
    c.create_rectangle(x-r,y-r,x+r,y+r, fill = "red")
    a = sirka - x
    b = vyska - y
    c.create_rectangle(a-r, y-r, a+r, y+r, fill = "red")
    c.create_rectangle(x-r, b-r, x+r, b+r, fill = "red")
    c.create_rectangle(a-r, b-r, a+r, b+r, fill = "red")
c.bind("<Motion>", pohyb)
