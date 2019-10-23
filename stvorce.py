import tkinter
import random

x_max, y_max = 800, 600

canvas = tkinter.Canvas(width=x_max, height=y_max)
canvas.pack()

def stvorec(x,y,p,v,m):
    v=1/2*v
    for i in range(1,p):
        
        canvas.create_rectangle(x-v,y-v,x+v,y+v)
        v=v-m



for i in range(10):
    x=random.randint(150,x_max-150)
    y=random.randint(150,y_max-150)
    v=random.randrange(150,301)
    p=random.randrange(5,11)
    m=10
    stvorec(x,y,p,v,m)
    
