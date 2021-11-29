from tkinter import *
from PIL import ImageTk

root = Tk()

root.geometry("700x600")
root.title("My first gui app")

#Important label options
# text - adds the text
# bd - background
# fg - foreground  (>Font colour<)
# font - sets the font
# padx - padding x
# pady - padding y
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text="'Desert'\n Is a vast land that is made full of mud and sand"
, bg="cyan", fg="purple", padx=104, pady=33, font="arial 19 bold"
 ,borderwidth=5,relief="sunken" )

# Important pack options
# 1.anchor=nw(n=north , w = west)
# 2.side = top , right , left , bottom (top by default)
# fill

title_label.pack(anchor="nw", fill=X , side = "top")

root.mainloop()