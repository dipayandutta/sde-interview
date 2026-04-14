from tkinter import *

root = Tk()

label = Label(root, text="Hello Python")
label.configure(text="Hello Tkinter", fg="red")
label.configure(bg="yellow")
label.configure(font="Monaco")
label.configure(wraplength="150")


label.pack()

root.geometry("400x300")
root.mainloop()
