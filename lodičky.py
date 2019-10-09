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


def mesiacik(x,y,r,f,h,m):
    canvas.create_oval(x,y,x+r,y+r,fill=f,outline=h)
    canvas.create_oval(x-m+r*0.5,y,x-m+r*1.5,y+r,fill=h,outline=h)

mesiacik(205,265,50,"red","green",0)

mesiacik(1420,275,30,"blue","red",0)
mesiacik(1380,275,30,"blue","red",30)

def lodka(x,y,c):
    canvas.create_polygon(x,y,x+c*0.5,y+0.5*c,x+c*1.5,y+c*0.5,x+2*c,y,fill="green",outline="black")
    canvas.create_rectangle(x+c*0.95,y,x+c*1.05,y-1.8*c,fill="brown",outline="black")
    canvas.create_polygon(x+c,y-1.8*c,x+1.5*c,y-0.5*c,x+c,y-0.3*c,fill="white",outline="black")
    mesiacik(x+1.1*c,y+0.1*c,c*0.3,"blue","green",0)
    mesiacik(x+0.6*c,y+0.1*c,c*0.3,"blue","green",(c*0.3))
x=random.randint(550,700)
y=425
z=100

for i in range(1,4):    
    lodka(x,y,z)
    x-=200
    y+=150
    z+=100





