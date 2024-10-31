from tkinter import *
from tkinter.ttk import Button
root = Tk()
root.title("title")
root.geometry("800x500")

def window2():
    root.destroy()
    window2_main = Tk()
    Label(window2_main, text="Bye Bye").pack()
    window2_main.mainloop()
    
a = Button(text="Click This", command=window2)
a.pack()
root.mainloop()
