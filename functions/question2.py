##create afunction in such a way that we can pass any number argements
#to this and it should display each argument's value
def arg(*args):
    for i in args:
        print(i)
arg("yash","2","3","4")    
