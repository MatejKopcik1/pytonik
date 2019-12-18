import tkinter
from random import randrange

sirka = 1280
vyska = 720

c = tkinter.Canvas(width = sirka, height = vyska)
c.pack()

r = 5

def klik(event):
    x, y = event.x, event.y
    c.create_oval(x-r, y-r, x+r, y+r, fill="red")
    global xx,yy
    xx, yy = x, y
def pusti(event):
    x, y = event.x, event.y
    c.create_oval(x-r, y-r, x+r, y+r, fill="blue")
    c.create_line(xx, yy, x, y)
    
c.bind("<ButtonPress>", klik)
c.bind("<ButtonRelease>", pusti)


