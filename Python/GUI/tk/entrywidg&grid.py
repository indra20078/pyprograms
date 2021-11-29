from tkinter import *

root = Tk()

def submit():
    print(f"the username is: {uservalue.get()}")
    print(f"the password is: {passvalue.get()}")

root.geometry("500x400")

username = Label(root, text = "Enter your username")
username.grid()

password = Label(root, text = "Enter your password")
password.grid(row=1)

# variable classes
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

btn = Button(text= "Submit", command=submit).grid()

root.mainloop()

