from tkinter import * 

root = Tk()

def getvals():
    print(n.get())
    print(d.get())
    print(j.get())
    print(e.get())
    print(h.get())
    print(chb.get())
    
    
root.geometry("500x400")

title = Label(root, text = "MY FORM ----created by idhs", font="arial 18 bold", pady=15).grid(row=0,column=3)
name = Label(root, text= "Name")
dob = Label(root, text= "DOB")
job = Label(root, text= "JOB")
ed = Label(root, text= "Education")
hob = Label(root, text= "Your hobby")

name.grid(row=1, column=2)
dob.grid(row=2, column=2)
job.grid(row=3, column=2)
ed.grid(row=4, column=2)
hob.grid(row=5, column=2)

n = StringVar()
d = StringVar()
j = StringVar()
e = StringVar()
h = StringVar()
chb = IntVar()

nam = Entry(root, textvariable=n)
do = Entry(root, textvariable=d)
jo = Entry(root, textvariable=j)
edu = Entry(root, textvariable=e)
ho = Entry(root, textvariable=h)


nam.grid(row=1, column=3)
do.grid(row=2, column=3)
jo.grid(row=3, column=3)
edu.grid(row=4, column=3)
ho.grid(row=5, column=3)

# CHECKBOX
cb = Checkbutton(text="I want to recieve updates", variable=chb, pady=14)
cb.grid(row=6, column=3)

btn = Button(root, text="Submit to ID", command=getvals)
btn.grid(row=7,column=3)

root.mainloop()