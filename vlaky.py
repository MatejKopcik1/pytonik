import tkinter
import random
canvas=tkinter.Canvas(width=1600, height=900)
canvas.pack()

def vlak(x,y,z,f):
    canvas.create_rectangle(x+z,y,x+17*z,y+8*z,fill=f)
    canvas.create_rectangle(x,y+6*z,x+z,y+7*z,fill="black")
    canvas.create_rectangle(x+17*z,y+6*z,x+18*z,y+7*z,fill="black")
    canvas.create_oval(x+3*z,y+6*z,x+7*z,y+10*z,fill="black")
    canvas.create_oval(x+11*z,y+6*z,x+15*z,y+10*z,fill="black")
    
z=random.randrange(1,10)

x=100
y=100
m=random.randrange(5,15)
for m in range(1,m):
    vlak(x,y,z,"red")
    x+=18*z

x=100
y=300
h=random.randrange(5,10)

for h in range(1,h):
    vlak(x,y,z,"yellow")
    x+=18*z

x=100
y=500
l=random.randrange(5,10)

for l in range(1,l):
    vlak(x,y,z,"blue")
    x+=18*z
