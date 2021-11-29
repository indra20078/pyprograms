print("Printing current and previous number and their sum in a given range input")
z = int(input("Enter the starting number: "))
a = int(input("Enter the Ending number: "))


b = z - 1
for c in range(z,a +1, 2):
    sum = c + b
    print("Current Number", c, "Previous Number ", b, " Sum: ", b + c)
    b = c

    #range(0,5,2)