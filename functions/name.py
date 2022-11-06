def name(firstName, lastName):
    print("My Name is",firstName +" "+lastName)
name("Yash","Tripathi")    
#def name(*args)-valid for any no of arguments
def name(*args):
    print(args)
    #to print any particular argument we write
    #print(args[0])
name("Yash","Tripathi","19","U.P.") 
name("shivam","tiwari")
#object or tuple
def name(name, *args):
    print(name)
    print(args)
    #to print any particular argument we write
    #print(args[0])
name("Yash","Tripathi","19","U.P.")
# assigning default value to parameters
def name(firstName="shivam",age=100):
    print("My Name is",firstName ,"my age is",age)
name("Yash") 
#name()
name("shubham",101)
#arbitrary key word arguments
def info(name,**data):
    print(name)
    print(data)
info("adhiraaaj",age=26,place="chandigarh",num=999999999)
#concept#**-makes dictionary,*-makes tuple
def info(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
info("Yash",age=18,place="Basti",num=999999999)        

