# # x = input("Enter you age: ")

# def my_method(age):
#     print(age * 3)

# my_method(43)

# my_method(55)

# #intermediate section..

# def my_method1(country = "India"):
#     print("my country is: "+country)

# my_method1()

# my_method1("Pakisthan")


# def my_method2(x):
#     return x * 5 

# number = my_method2(6)
# print(number)

# x = input("ENter your 1st brands: ")
# y = input("ENter your 2nd brands: ")
# z = input("ENter your 3rd brands: ")

# def my_brands(brand1,brand2,brand3):
#     print("your second brand is: " +brand2 )

# my_brands(x,y,z)


#Advanced section   Arbitary arguments

def my_hobbies(*hobbies):   #  * converts to tuple
    print("your last hobby entered is: "+hobbies[-1])

my_hobbies("programming","cricket","Playing video games")

# y= input("Enter brand name: ")
# x = input("ENter model name: ")

def my_brand(**brand):   #  ** converts to dictionary
    print("your brand model is: " +brand["model"])

my_brand(brand = "apple" , model = "iphonex")



