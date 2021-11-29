import time

a = input("Enter a variable you want find out: ")#3*x
b = float(input("Enter the the value you want to add with the variable: "))#6
c = float(input("Enter the result: "))#12
if "*" in a:
    d = a.split("*")#[3,x]
    z = float(d[0])
    q = d[1]
    a = c - b
    print("the value of ",q," is " ,int(a)/z)
elif "+" in a:
    d = a.split("+")#[3,x]
    z = float(d[0])
    q = d[1]
    a = c - b#6
    print("the value of ",q," is " ,a-z)
elif "-" in a:
    d = a.split("-")#[3,x]
    z = float(d[0])
    q = d[1]
    a = c - b#6
    print("the value of ",q," is " ,a+z)
elif "/" in a:
    d = a.split("/")#[3,x]
    z = float(d[0])
    q = d[1]
    a = c - b#6
    print("the value of ",q, "is ",a*z)
else:
    q = a[0]
    a = c - b
    print("the value of",q," is: ", a)
