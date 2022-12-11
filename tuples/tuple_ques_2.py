# write a program to unpack folllowing tuple
# into 4 variables
tuple1=(10,20,30,40,)
# (a,b,c,d,)=tuple1                    #method 1
# print(a)
# print(b)
# print(c)
# print(d)
# for i in tuple1:                      # method 2
#     print(i)
l=len(tuple1)                          #method3
ind=0
while l!=0:
    print(tuple1[ind])
    ind+=1
    l-=1

