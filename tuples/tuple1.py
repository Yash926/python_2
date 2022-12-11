# myTuple=(1,2,3,4,4)           #introduction of tuple
# print(len(myTuple))
# print(myTuple)
# tuple1=("apple",)
# # print(tuple1)
# tuple2=("car","bike","boat","jet")
# print(tuple2[1])#for indexing we will use [] bracket
# print(tuple2[1:3])
# list1=list(tuple2)
#                             #to make any chnage in tuple type cast it to list and then again type cast it to tuple
# list1.append("cycle")
# tuple3=tuple(list1)
# print(tuple3)
#                             #here 6,7 both are assigned as  same index 3 (which is a list)
# tuple4=(1,2,3,[6,7],4,4)
# # print(tuple4[3][0])
# tuple4[3][0]=8
# print(tuple4)
#                              #swap the tuples
# tuple5=(10,20)
# tuple6=(30,40)
# temp=tuple5

# tuple5=tuple6
# tuple6=temp
# print(tuple5)
# print(tuple6)
# tuple7=(1,2,3)                  #packing and unpacking
# (one,two,three)=tuple1
# print(one)
# print(two)
# print(three)

#tuple8=("car","bike","boat","cycle")         #packing
# (item1,*item2,item3)=tuple1                  #unpacking
# print(item1)
# print(item2)
# print(item3)

tuple9=(10,20,30,40)
tuple10=(tuple9[1],tuple9[2])
print(tuple10)





