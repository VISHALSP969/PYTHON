import tkinter
from tkinter import messagebox

top = tkinter.Tk()


def helloCallBack():
    messagebox.showinfo('Hello Python', 'Hello World')


B = tkinter.Button(top, text='Hello', command=helloCallBack)

B.pack()
top.mainloop()
