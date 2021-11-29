from tkinter import *
from PIL import Image, ImageTk
root = Tk()

root.geometry("795x675")

#inserting an image
#opening .jpg images 

photo = ImageTk.PhotoImage(file="1.jpg")


root1 = Label(image=photo).pack()




root.mainloop()