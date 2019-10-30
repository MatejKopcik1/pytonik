import tkinter
import random
canvas=tkinter.Canvas(width=1600,height=900,background="lightgreen")
canvas.pack()

def strom(x,y,z):
    canvas.create_rectangle(x,y,x+16,y-200,fill="brown")
    canvas.create_oval(x+9-z,y-200-z,x+9+z,y-200+z,fill="green")

for i in range(1,11):
    x=random.randint(50,1500)
    y=random.randint(150,600)
    z=random.randrange(35,100)
    strom(x,y,z)
    

def trava(x,y):
    h=random.randrange(3,20)
    for i in range(1,h):
        d=random.randrange(-20,20)
        f=random.randrange(1,60)
        s=random.randrange(1,3)
        canvas.create_line(x,y,x+d,y-f,fill="green",width=s)





for i in range(1,21):
    
    x=random.randint(20,1600)
    y=random.randint(60,900)
    trava(x,y)
