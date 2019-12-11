import tkinter
import random
import math

c=tkinter.Canvas(width=800, height=800, bg="black")
c.pack()


while True:
    
    def sekundova(x,y,s,m,h,r):
        for j in range(43200):
            c.delete("all")
            c.create_oval(0,0,800,800,fill="white")
            
            u=j * 2*(math.pi)/s - (math.pi)/2
            
            
            a=x + math.cos(u) * r
            b=y + math.sin(u) * r
            c.create_line(x,y,a,b,fill="black",width=1)
            
    
            u=j * 2*(math.pi)/m - (math.pi)/2
            a=x + math.cos(u) * r*0.9
            b=y + math.sin(u) * r*0.9
            c.create_line(x,y,a,b,fill="black",width=2)

            u=j * 2*(math.pi)/h - (math.pi)/2
            a=x + math.cos(u) * r*0.8
            b=y + math.sin(u) * r*0.75
            c.create_line(x,y,a,b,fill="black",width=4)
            
            c.after(1000)
            c.update()

            
    x=400
    y=400


    sekundova(x,y,60,3600,43200,350)
