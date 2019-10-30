import tkinter
import random

plocha_s = 1600
plocha_v = 900

canvas=tkinter.Canvas(width=plocha_s, height=plocha_v, background="white")

canvas.pack()

canvas.create_rectangle(0,(plocha_v)/2,plocha_s,plocha_v,fill="blue")

def mesiac(x,y,r,f,h,z,m):
    
    canvas.create_oval(x,y,x+r,y-z,fill=f,outline=h)
    
    canvas.create_oval(x-m+(r/2),y,x-m+(r*1.5),y-z,fill=h,outline=h)
    


v=random.randrange(100,350)

z=plocha_s/16

mesiac((plocha_s/16*10),(plocha_v/2)-(-v),100,"yellow","blue",z,0)

mesiac((plocha_s/16*10),(plocha_v/2)-v,100,"yellow","white",-z,0)


def ostrov(x,y,g):
    
    canvas.create_oval(x,y,x+250,y+250,fill="brown")
    
    canvas.create_line(x+125,y,x+125,y-50)
    
    canvas.create_rectangle(x+125,y-170,x+305,y-50,fill=g)
    
    canvas.create_rectangle(x,450,x+250,700,fill="blue",outline="blue")
    

ostrov((plocha_s/16)/5,(plocha_v/2)-50,"green")

ostrov((plocha_s/16)*12,(plocha_v/2)-50,"red")

mesiac(205,265,50,"red","green",(-50),0)

mesiac(1420,275,30,"blue","red",(-30),0)

mesiac(1380,275,30,"blue","red",(-30),30)


def lodka(x,y,c):
    
    canvas.create_polygon(x,y,x+c*0.5,y+0.5*c,x+c*1.5,y+c*0.5,x+2*c,y,fill="green",outline="black")
    
    canvas.create_rectangle(x+c*0.95,y,x+c*1.05,y-1.8*c,fill="brown",outline="black")
    
    canvas.create_polygon(x+c,y-1.8*c,x+1.5*c,y-0.5*c,x+c,y-0.3*c,fill="white",outline="black")
    
    mesiac(x+1.1*c,y+0.1*c,c*0.3,"blue","green",-(c*0.3),0)
    
    mesiac(x+0.7*c,y+0.1*c,c*0.3,"blue","green",-(c*0.3),(c*0.3))
    
    
x=random.randint(550,700)
y=plocha_v/2+25
z=plocha_s/16

for _ in range(1,4):
    
    lodka(x,y,z)
    x-=200
    y+=150
    z+=100





