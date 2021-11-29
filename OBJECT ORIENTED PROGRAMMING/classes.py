# class MyClass:
#     x = int(input("Enter a numer to add: "))
#     y = int(input("ENter another number: "))
#     print(x + y)

# calculation_add = MyClass   # here calculation_add is called as instances

class Employees:
    def __init__(self , name, salary, attendance):#__init__ is a constructor of variables
        self.name = name
        self.salary = salary
        self.attendence = attendance

    def show_employee_details(self):
        print("Name: " +self.name , ", Salary: " +self.salary, ", Attendence: "+self.attendence)

    def attendence_check(self):
        print("Name: " +self.name, ", Salary: " +self.salary ,  ", Attendence: "+self.attendence)

x =  input("Enter the employee name: ")
y =  input("Enter employee's salary: ")
z =  input("Enter the employee's attendence (True/False): ")
a =  input("Which one do you want to check of employee(attendence/details): ")

if a == "details" or a == "Details":
    employe = Employees(x , y , z)
    employe.show_employee_details()

elif a == "attendence" or a == "Attendence":
    employee = Employees(x , y , z)
    employee.attendence_check()

else:
    print("Try again")
    


