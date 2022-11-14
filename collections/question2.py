numbers=[1,2,3,4,5,2,6]
#in the above list find value of 2, if it is present
# replace it with 200 only update the first occurence
num=[]
count=0
for i in numbers:
    if i==2 and count==0:
        i=200
        num.append(i)
        count+=1
    else:
        num.append(i)
print(num)
#method 2
indx=numbers.index(2)
numbers[indx]=200
print(numbers)

