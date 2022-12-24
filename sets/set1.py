
#set-stores multiple values to single variable
#unordered
#unchangable/immutable
#duplicates not allowed
#non-homogeneous
myset={"car","boat","train","car"}
myset1={"car","boat","train","car"}
myset2={1,2,3,4}
myset3={4,5,6,7}
output1=myset2.intersection(myset3)
print(output1)
output2=myset2.symmetric_difference(myset3)         #to get non common elements
print(output2)
output=myset2.union(myset3)               # to get union of 2 sets not allowing duplicate values
print(output)
myset1.update({"cycle","bus","shivam"})                     #to update or add 2 sets or add multiple elements
myset1.update(myset2)
print(myset1)
print(myset)
myset.add("cycle")                        #to add something to our set
print(myset)

# set1={"car","bike","boat"}
# if "boat" in set1:
#     print("boat")
