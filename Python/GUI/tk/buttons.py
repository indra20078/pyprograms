from tkinter import *

root = Tk()

def hello():
    print("hello world!!!")

def q():
    print("whatsapp guys")

def w():
    print("Hey there!! hope you will have a nice day")

def e():
    print("Whatsapp broo")

f1 = Frame(root , borderwidth=6 , bg = "grey", )
f1.pack()

b1 = Button(f1 , fg = "black" , text = "Print now" , command = hello)
b1.pack(side = RIGHT)

b2 = Button(f1 , fg = "black" , text = "wu" , command = e)
b2.pack(side = RIGHT)

b3 = Button(f1 , fg = "black" , text = "hyhnd" , command = w)
b3.pack(side = RIGHT)

b4 = Button(f1 , fg = "black" , text = "chat" , command = q)
b4.pack(side = RIGHT)

root.mainloop()