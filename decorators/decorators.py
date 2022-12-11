def div(a,b):# this func is unchangeble
    print(a/b)
div(4,2)
def  new_div(func): #taking function asa parameter

    def inner_func(a,b): #function containing same parameters as original function
        if a<b:
            a,b=b,a #swappping
        return func(a,b)
    return inner_func
div=new_div(div)
div(2,4)