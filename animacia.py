import tkinter

c = tkinter.Canvas(width = 1600, height = 900)
c.pack()

x, y = 100, 100
for _ in range(1,600):
    c.delete("all")
    idd = c.create_rectangle(x, y, x + 50, y + 50)
    x+=1
    c.update()
    c.after(20)
    print (idd)
