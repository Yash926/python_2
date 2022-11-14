colors=["red","blue","black","orange"]
cars=["TATA","NANO","ALTO"]
players=("Dhoni","virat","dravid")
numbers=[1,4,6,8,2]
#copying elements of one list to other list
num2=numbers.copy()
print(num2)
#method 2 of copying
num2=list(numbers)
print(num2)
#concatenation(happens on the same data type)
list1=["x","y","z"]
list2=[1,2,3]
#method1
list3=list1+list2
print(list3)
#method2
for x in list2:
    list1.append(x)
print(list1)
#method3
list1.extend(list2)
print(list1)

