from tkinter import *
from random import randint
def clicked(event):
    global score,counter
    if str(event.widget)[2:] == "button": score+=1
    else: score = 0
    counter.configure(text=  score)
    print(score)
size = 200
score = 0
geometry = str(200) + "x" + str(200)
root = Tk()
root.bind("<Button-1>", clicked)
root.resizable(False, False)
root.geometry(geometry)
counter = Label(root, fg = "red", text = score)
counter.pack(side = TOP)
b = Button(root,bg = "black", width = 2, height = 1, command = lambda:b.place(x=randint(0,size-10),y=randint(0,size-10)))
b.place(x=randint(0,size),y=randint(0,size))
root.mainloop()