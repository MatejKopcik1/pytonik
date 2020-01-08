import tkinter

sirka = 1536
vyska = 864

c = tkinter.Canvas(width = sirka, height = vyska, bg="white")
c.pack()

r = 50

c.create_rectangle(sirka,vyska,sirka-r,vyska-r,fill="red")
c.create_rectangle(sirka-2*r,vyska,sirka-r,vyska-r,fill="blue")
c.create_rectangle(sirka-3*r,vyska,sirka-2*r,vyska-r,fill="green")
c.create_rectangle(sirka-4*r,vyska,sirka-3*r,vyska-r,fill="yellow")
c.create_rectangle(sirka-5*r,vyska,sirka-4*r,vyska-r,fill="black")
c.create_rectangle(sirka-6*r,vyska,sirka-5*r,vyska-r)

c.create_rectangle(5, vyska-r, r+5, vyska,)
c.create_oval(15,vyska-r+10,r-5,vyska-10,fill="black")

c.create_rectangle(5+r, vyska-r, 2*r+5, vyska,)
c.create_oval(20+r,vyska-r+15,2*r-10,vyska-15,fill="black")

c.create_rectangle(5+2*r, vyska-r, 3*r+5, vyska,)
c.create_oval(25+2*r,vyska-r+20,3*r-15,vyska-20,fill="black")

c.create_rectangle(5+3*r, vyska-r, 4*r+5, vyska,)
c.create_oval(28+3*r,vyska-r+23,4*r-18,vyska-23,fill="black")

c.create_rectangle(sirka-r, 5, sirka, r+5)
c.create_rectangle(sirka-r+15,10,sirka-15,20,fill="grey")
c.create_rectangle(sirka-r+15,20,sirka-15,50)

c.create_rectangle(sirka-r,r+10,sirka,2*r+10)
c.create_line(sirka-r+5,r+15,sirka-5,2*r+5,width=3,fill="red")
c.create_line(sirka-r+5,2*r+5,sirka-5,r+15,width=3,fill="red")

c.create_rectangle(5,5,r+5,r+5)
c.create_rectangle(15,20,45,25,fill="black")
c.create_polygon(15,25,20,45,40,45,45,25,fill="white",outline="black")

c.create_rectangle(r+10,r+10,sirka-r-10,vyska-r-10)
k = False
farba = "black"
hrubka = 1

def press(event):
    
    global xpress, ypress
    global k
    global farba
    global farba_pozadia
    global hrubka
    
    xpress = event.x
    ypress = event.y
    
    k = True
    
    if 5 < xpress < r+5 and 5 < ypress < r+5:
        c.create_rectangle(r+10,r+10,sirka-r-10,vyska-r-10,fill=farba)
        farba_pozadia = farba
        
    if sirka-4*r < xpress < sirka-3*r and vyska - r < ypress < vyska:
        farba="yellow"
    elif sirka-3*r < xpress < sirka-2*r and vyska - r < ypress < vyska:
        farba="green"
    elif sirka-2*r < xpress < sirka -r and vyska -r < ypress < vyska:
        farba="blue"
    elif sirka -r < xpress < sirka and vyska -r < ypress < vyska:
        farba = "red"
    elif sirka-5*r < xpress < sirka-4*r and vyska-r < ypress < vyska:
        farba="black"
    elif sirka-6*r < xpress < sirka-5*r and vyska-r < ypress < vyska:
        farba="white"
    elif sirka-r < xpress < sirka and 5 < ypress < r+5:
        farba = farba_pozadia
        hrubka = 20

    

    if 5 < xpress < r+5 and vyska - r < ypress < vyska:
        hrubka = 15
    elif 5 + r < xpress < 2*r + 5 and vyska - r < ypress < vyska:
        hrubka = 10
    elif 5 + 2*r < xpress < 3*r + 5 and vyska - r < ypress < vyska:
        hrubka = 5
    elif 5 + 3*r < xpress < 4*r + 5 and vyska - r < ypress < vyska:
        hrubka = 1

    if sirka-r < xpress < sirka and r+10 < ypress < 2*r+10:
        c.delete("all")
        c.create_rectangle(sirka,vyska,sirka-r,vyska-r,fill="red")
        c.create_rectangle(sirka-2*r,vyska,sirka-r,vyska-r,fill="blue")
        c.create_rectangle(sirka-3*r,vyska,sirka-2*r,vyska-r,fill="green")
        c.create_rectangle(sirka-4*r,vyska,sirka-3*r,vyska-r,fill="yellow")
        c.create_rectangle(sirka-5*r,vyska,sirka-4*r,vyska-r,fill="black")
        c.create_rectangle(sirka-6*r,vyska,sirka-5*r,vyska-r)
        
        c.create_rectangle(5, vyska-r, r+5, vyska,)
        c.create_oval(15,vyska-r+10,r-5,vyska-10,fill="black")

        c.create_rectangle(5+r, vyska-r, 2*r+5, vyska,)
        c.create_oval(20+r,vyska-r+15,2*r-10,vyska-15,fill="black")

        c.create_rectangle(5+2*r, vyska-r, 3*r+5, vyska,)
        c.create_oval(25+2*r,vyska-r+20,3*r-15,vyska-20,fill="black")

        c.create_rectangle(5+3*r, vyska-r, 4*r+5, vyska,)
        c.create_oval(28+3*r,vyska-r+23,4*r-18,vyska-23,fill="black")

        c.create_rectangle(sirka-r, 5, sirka, r+5)
        c.create_rectangle(sirka-r+15,10,sirka-15,20,fill="grey")
        c.create_rectangle(sirka-r+15,20,sirka-15,50)

        c.create_rectangle(sirka-r,r+10,sirka,2*r+10)
        c.create_line(sirka-r+5,r+15,sirka-5,2*r+5,width=3,fill="red")
        c.create_line(sirka-r+5,2*r+5,sirka-5,r+15,width=3,fill="red")

        c.create_rectangle(5,5,r+5,r+5)
        c.create_rectangle(15,20,45,25,fill="black")
        c.create_polygon(15,25,20,45,40,45,45,25,fill="white",outline="black")

        c.create_rectangle(r+10,r+10,sirka-r-10,vyska-r-10)

        
def release(event):
    global k
    k = False

def motion(event):
    global xpress, ypress
    xmotion = event.x
    ymotion = event.y
    
    if k == True:
        c.create_line(xpress, ypress, xmotion, ymotion,fill=farba,width=hrubka)
        xpress, ypress = xmotion, ymotion
    
c.bind("<ButtonPress>", press)
c.bind("<ButtonRelease>", release)
c.bind("<Motion>", motion)


