import tkinter
from random import randrange, randint

x_max = 1600
y_max = 900

c=tkinter.Canvas(width=x_max, height=y_max, bg="black")
c.pack()

r = 20
x, y = 10* randint(r/10, (x_max-r)/10), 10* randint(r/10, (y_max-r)/10)

g = 10
k = 10

while True:
    
    f = c.create_rectangle(x-r, y-r, x+r, y+r, fill="red")
    
    x= x + g
    y= y+k

    if x >= x_max - r:
        g = -10
        
    if x <= r:
        g = 10
        
    if y >= y_max - r:
        k = -10

    if y <= r:
        k = 10
        
    
        
    c.update()
    c.after(20)
    c.delete(f)
    
    if y-r == 0 and x-r == 0:
        c.delete("all")
    
    if y+r == y_max and x+r == x_max:
        c.delete("all")

    if y-r == 0 and x+r == x_max:
        c.delete("all")

    if y+r == y_max and x-r == 0:
        c.delete("all")
        
