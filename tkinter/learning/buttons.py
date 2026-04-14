"""
Tkinter to create Buttons
"""

from tkinter import *

root = Tk()


def callback():
    label.config(text="You Clicked Me!", fg="red", bg="yellow")


label = Label(root, text="Hello Python!")
label.pack()

button = Button(root, text="Button", command=callback)
button.pack()

root.geometry("400x300")
root.mainloop()
