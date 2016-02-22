# -*- coding: utf-8 -*- 

from tkinter import *
from tkinter.messagebox import showinfo

top = Tk()

C = Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()
