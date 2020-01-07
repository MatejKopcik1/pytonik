import tkinter
from random import randrange

vy = 900
si = 1600

c = tkinter.Canvas( height = vy, width = si, bg = "white" )
c.pack()



def s():
    for _ in range(100):
        x,y = randrange(50,1550),randrange(50,850)
        c.create_oval( x-5, y-5, x+5, y+5, fill = "lightblue" )

while True:
    c.delete("all")
    s()
    c.after(100)
    c.update()
    
