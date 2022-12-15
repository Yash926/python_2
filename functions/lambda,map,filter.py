def isEven(i):
    return i%2==0
    #method 1
list1=[3,2,8,16,11,34]
output=list(filter(isEven,list1))       #filter is itself a function taking function as argument
print(output)
#mehod 2
output1=list(filter(lambda i: i%2==0,list1)) 
print(output1)
output3=list(filter(lambda i: i>15,list1)) 
print(output3)
output4=list(map(lambda i:i+2,list1))  # going to every element an doing the alloted change to every element
print(output4)
output5=list(map(lambda i:i**2,list1))
print(output5)

from functools import reduce          
output6=reduce(lambda a,b:a+b,list1)
print(output6)