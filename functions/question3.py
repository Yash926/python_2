# Create a function using following instruction
# it should acccept employee name and salary and display both
# if the salary is missing in the function then assign default 10000 to salary
# ben(90000) mike(15000) bob()
def num(empname,empsalary=10000):
    print("the salary of "+empname,"is",empsalary)
num("Ben",9000)
num("Mike",15000)
num("Bob")    