from platform import python_branch
from tkinter import *

root = Tk()

wwidth = 500
hheight = 400

can_width = 500
can_height = 400

root.geometry(f"{wwidth}x{hheight}")

can = Canvas(root, width=can_width, height=can_height)
can.pack()

# x1,y1 to x2, y2 (coordinate geometry)
can.create_line(0, 600, 300, 0,fill="red")
can.create_line(0, 0, 300, 600, dash=7)

root.mainloop()

