import tkinter
import random

sirka = 1536
vyska = 864

c = tkinter.Canvas(width = sirka, height = vyska)
c.pack()

r = 50

c.create_rectangle(sirka,vyska,sirka-r,vyska-r,fill="red")
c.create_rectangle(sirka-2*r,vyska,sirka-r,vyska-r,fill="blue")
c.create_rectangle(sirka-3*r,vyska,sirka-2*r,vyska-r,fill="green")
c.create_rectangle(sirka-4*r,vyska,sirka-3*r,vyska-r,fill="yellow")

c.create_rectangle(5, vyska-r, r+5, vyska,)
c.create_oval(15+r,vyska-r+10,2*r-5,vyska-10,fill="black")

c.create_rectangle(5+r, vyska-r, 2*r+5, vyska,)
c.create_oval(15,vyska-r+10,r-5,vyska-10,fill="black")

c.create_rectangle(5+2*r, vyska-r, 3*r+5, vyska,)
c.create_oval(15,vyska-r+10,r-5,vyska-10,fill="black")

k = False
farba = "black"
w = 1
def press(event):
    global xpress, ypress
    global k
    global farba
    global w
    xpress = event.x
    ypress = event.y
    k = True
    if sirka-4*r < xpress < sirka-3*r and vyska - r < ypress < vyska:
        farba="yellow"
    elif sirka-3*r < xpress < sirka-2*r and vyska - r < ypress < vyska:
        farba="green"
    elif sirka-2*r < xpress < sirka -r and vyska -r < ypress < vyska:
        farba="blue"
    elif sirka -r < xpress < sirka and vyska -r < ypress < vyska:
        farba = "red"
    

def release(event):
    global k
    k = False

def motion(event):
    global xpress, ypress
    xmotion = event.x
    ymotion = event.y
    
    if k == True:
        c.create_line(xpress, ypress, xmotion, ymotion,fill=farba,width=w)
        xpress, ypress = xmotion, ymotion
    
c.bind("<ButtonPress>", press)
c.bind("<ButtonRelease>", release)
c.bind("<Motion>", motion)



