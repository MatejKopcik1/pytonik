import tkinter
import random
canvas=tkinter.Canvas(width=1600, height=900, background="white")
canvas.pack()

canvas.create_rectangle(0,450,1600,900,fill="blue")
y=random.randrange(100,350)
z=100

def mesiac(y,f,z):
    canvas.create_oval(1050,450-y,1150,450-y-z,fill="yellow",outline=f)
    canvas.create_oval(1100,450-y,1200,450-y-z,fill=f,outline=f)


mesiac(-y,"blue",z)

mesiac(y,"white",-z)

##koniec 1. ulohy

def ostrov(x,y,g):
    canvas.create_oval(x,y,x+250,y+250,fill="brown")
    canvas.create_line(x+125,y,x+125,y-50)
    canvas.create_rectangle(x+125,y-170,x+305,y-50,fill=g)
    canvas.create_rectangle(x,450,x+250,700,fill="blue",outline="blue")

ostrov(20,400,"green")
ostrov(1200,400,"red")




##canvas.create_oval(1050,450-y,1150,450-y-z,fill="yellow",outline=f)
##canvas.create_oval(1100,450-y,1200,450-y-z,fill=f,outline=f)


def mesiacik(x,y,r,f):
    canvas.create_oval(x,y,x+r,y+r,fill=f,outline="green")
    canvas.create_oval(x+r/2,y,x+r,y+r,fill="green",outline="green")

mesiacik(205,265,50,"red")













