from tkinter import *

root = Tk()

def submit():
    print(a.get())
    print(b.get())

root.geometry("500x400")

u = Label(root, text= "Enter dancers names")
v = Label(root, text= "Enter dancing style")
u.grid()
v.grid(row=1)

a = StringVar()
b = StringVar()

c = Entry(root, textvariable=a)
d = Entry(root, textvariable=b)
btn = Button(text= "Submit", command=submit).grid()

c.grid(row=0, column=1)
d.grid(row=1, column=1)

root.mainloop()