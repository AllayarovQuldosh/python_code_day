from tkinter import*
from tkinter.ttk import *
from time import strftime

root = Tk()

def time():
    string = strftime('%H:%M:%S %a')
    label.config(text = string)
    label.after(1000, time)

label = Label(root, font=("",100),background = "black",foreground = "white")
label.pack(anchor = 'center')
time()
mainloop()