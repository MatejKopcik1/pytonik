import tkinter
from random import randrange

v = 900
s = 1600

c=tkinter.Canvas(width = s, height = v, bg = "white")
c.pack()

 
while True:
    r = randrange(0,255)
    g = randrange(0,255)
    b = randrange(0,255)
    farba = f"#{r:02x}{b:02x}{g:02x}"
    c.create_rectangle(200,200,400,400,fill = farba)
    c.after(100)
    c.update()
    
