import tkinter
from random import randrange

v = 900
s = 1600

c=tkinter.Canvas(width = s, height = v, bg = "white")
c.pack()

r = randrange(0,255)
g = randrange(0,255)
b = randrange(0,255)
j = 1

while True:
    c.delete("all")
    farba = f"#{r:02x}{g:02x}{b:02x}"

    b = b+j

    if b == 255:
        b = 0
        g += j

    if g == 255:
        g = 0
        b += j

    if r == 255:
        r = 0
    
    c.create_rectangle(200,200,400,400,fill = farba)
    t = c.create_text(500,500,text=farba, font="Times 40")
  
    c.after(1)
    c.update()
    
