# write a program to display onlythose numbers
# from a list tha satisfy following Condition

# number must be divisible by 5
# if the number is greater than 150,then skip it and move to next numbers
# if the number is 500,stop the loop
# number=[12,75,150,180,145]
list=[12,75,150,180,145]
for i in list:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)