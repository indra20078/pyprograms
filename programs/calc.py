print("Supported operations:\n**(power)\n*(multiplication)\n%(modulo)\n+ and -")
print("Enter the numbers you want to calculate with a sign:")
a = input()
try:
    if "+" in a:
        b,c = a.split("+")
        print(float(b) + float(c))
    elif "**" in a:
        b,c = a.split("**")
        print(float(b) ** float(c))
    elif "/" in a:
        b,c = a.split("/")
        print(float(b) / float(c))
    elif "-" in a:
        b,c = a.split("-")
        print(float(b) - float(c))
    elif "*" in a:
        b,c = a.split("*")
        print(float(b) * float(c))
    elif "%" in a:
        b,c = a.split("%")
        print(float(b) % float(c))
    else:
        print("Some error has occured please try again with proper input!!")

except(KeyboardInterrupt,ValueError):
    print("wrong input")
