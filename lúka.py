import tkinter
import random
canvas=tkinter.Canvas(width=1600,height=900,background="lightgreen")
canvas.pack()

def strom(x,y,z):
    canvas.create_rectangle(x,y,x+16,y-200,fill="brown")
    canvas.create_oval(x+9-z,y-200-z,x+9+z,y-200+z,fill="green")

x=random.randint(50,1500)
y=random.randint(150,450)
z=random.randrange(35,100)
for i in range(1,11):
    strom(x,y,z)
    x=random.randint(50,1500)
    y=random.randint(150,600)
    z=random.randrange(35,100)
