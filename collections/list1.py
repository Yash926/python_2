colors=["red","blue","black","orange"]
cars=["TATA","NANO","ALTO"]
players=("Dhoni","virat","dravid")
numbers=[1,4,6,2,8]
numbers.sort(reverse=True)
print(numbers)
# numbers.sort()
# print(numbers)
# newList=[x.lower() for x in cars]
# print(newList)

# method1
# [print(i) for i in cars if "A" in i]
# method2
# newList=[]
# for i in cars:
#     if "A" in i:
#         newList.append(i)
# print(newList)
#method3
# newList=[x for x in cars if x!= "TATA"]
# print(newList)
# [print(x) for x in cars]
# for x in range(len(cars)):
#     print(cars[x])
# x=0
# while x <len(cars):
#     print(cars[x])
#     x+=1

# colors[2]="green"
# colors[0:2]="yellow","white"
# print(colors[1:4])
# colors.insert(2,"indigo")
# colors.append("BMW")
# colors.extend(cars)
# colors.extend(players)
#colors.remove("red")
#pop removes from a specific index
#colors.pop(1)
# del colors[1]
#colors.clear()

# print(colors)