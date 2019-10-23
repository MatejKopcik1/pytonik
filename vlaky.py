import tkinter
import random
canvas=tkinter.Canvas(width=1600, height=900)
canvas.pack()

def vlak(x,y,f):
    canvas.create_rectangle(x,y,x+80,y+40,fill=f)
    canvas.create_rectangle(


vlak()
