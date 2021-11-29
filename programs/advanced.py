a = input("Enter the equation that contains a variable in the first term (for ex - 3x + 6 = 12): ")
b = a.split() 
c = b[0] 
d = b[1] 
e = b[2] 
f = b[3] 
g = b[4]           
h = c[0]
i = c[1]
try:
    if "+" in a:
        j = float(g) - float(e)
        z = j / float(h)
        print("The value of",i,"is",z)
    elif "-" in a:
        j = float(g) + float(e)
        z = j / float(h)
        print("The value of",i,"is",z)
    elif "/" in a:
        j = float(g) * float(e)
        z = j / float(h)
        print("The value of",i,"is",z)
    elif "*" in a:
        j = float(g) / float(e)
        z = j / float(h)
        print("The value of",i,"is",z)
except(IndexError):
        if "*" in a:
            z = e / float(h)
            print("The value of",i,"is",z)
        elif "/" in a:
            z = e * float(h)
            print("The value of",i,"is",z)
        elif "+" in a:
            z = e - float(h)
            print("The value of",i,"is",z)
        elif "-" in a:
            z = e + float(h)
            print("The value of",i,"is",z)
