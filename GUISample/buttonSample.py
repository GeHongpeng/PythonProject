# -*- coding: utf-8 -*- 

from tkinter import *
from tkinter.messagebox import showinfo

top = Tk()
top.title("My Helloworld")

def helloCallBack():
   showinfo(title="Hello Python", message="Hello World!")

B = Button(top, text ="Hello,Python!", command = helloCallBack)

B.pack()
top.mainloop()
