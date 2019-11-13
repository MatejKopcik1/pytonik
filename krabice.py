import tkinter
import random

s=800
v=450

c=tkinter.Canvas(width=s, height=v)
c.pack()

def krabica(x,y,f):
    c.create_rectangle(x,y,x+80,y-80,fill=f)
    c.create_line(x,y,x+80,y-80,width=5,fill="lightgreen")
    c.create_line(x,y-80,x+80,y,width=5,fill="light green")

x=110
y=400
z=random.randrange(1,6)

for v in range(z):
    krabica(x,y,"red")
    y-=80


x=210
y=400
z=random.randrange(1,6)

for _ in range(z):
    krabica(x,y,"yellow")
    y-=80

x=310
y=400
z=random.randrange(1,6)

for l in range(z):
    krabica(x,y,"orange")
    y-=80

x=410
y=400
z=random.randrange(1,6)

for m in range(z):
    krabica(x,y,"blue")
    y-=80
