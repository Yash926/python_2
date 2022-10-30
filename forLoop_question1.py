#write a program to accept a number from a user
# to calculate the sum of all numbers from
# 1 to given nnumber
# eg-user input 10
# output should be 55
# 1+2+3+4+5+6+7+8+9+10
user=int(input("enter number here:"))
count=0
for i in range(1,user+1):
    count=count+i
print("total sum is:",count)


