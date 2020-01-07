import tkinter
import random

vy = 900
si = 1600

c = tkinter.Canvas(width = si, height = vy, bg = "white")
c.pack()

k = False
c.create_line(0,vy/2,si,vy/2)
c.create_line(si/2,0,si/2,vy)
def press(event):

    global xpress, ypress, k
    
    xpress = event.x
    ypress = event.y

    k = True

def release(event):
    global k
    k = False

def motion(event):
    global xpress, ypress
    xmotion = event.x
    ymotion = event.y

    if k == True:
        c.create_line(xpress,ypress,xmotion,ymotion)
        
        
        n = si/2-xpress
        m = vy/2-ypress
        j = si/2-xmotion
        l = vy/2-ymotion
        c.create_line(xpress+2*n,ypress,xmotion+2*j,ymotion)
        c.create_line(xpress,ypress+2*m,xmotion,ymotion+2*l)
        c.create_line(xpress+2*n,ypress+2*m,xmotion+2*j,ymotion+2*l)
                   
        xpress,ypress = xmotion,ymotion

c.bind("<ButtonPress>", press)
c.bind("<ButtonRelease>", release)
c.bind("<Motion>", motion)
