# -*- coding: utf-8 -*- 

from tkinter import *
from tkinter.messagebox import showinfo

top = Tk()

checkVar1 = IntVar()
checkVar2 = IntVar()

C1 = Checkbutton(top, text="Music", variable=checkVar1, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)

C2 = Checkbutton(top, text="Video", variable=checkVar2, \
                 onvalue=1, offvalue=0, height=5, \
                 width=20)

C1.pack()
C2.pack()

top.mainloop()
