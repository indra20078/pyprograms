from tkinter import *

root = Tk()

root.geometry("600x500")
f1 = Frame(root, bg = "blue", borderwidth= 6, relief = GROOVE)
f1.pack(side=LEFT , fill=Y)

f2 = Frame(root, bg = "blue", borderwidth= 9, relief = GROOVE)
f2.pack(fill=X)

l = Label(f1, text = "My gui window" )
l.pack(fill = Y, pady=20)

l2 = Label(f2, text = "WELCOME!!", font = "Helvetica 14 bold" )
l2.pack()

root.mainloop()