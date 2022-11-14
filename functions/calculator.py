
def cal(input1,input2,opt):
    if opt==0:
        print(input1+input2)
    elif opt==1:
        print(input1-input2)
    elif opt==2:
        print(input1*input2)
    elif opt==3:
        print(input1/input2)
    else:
        print("invalid input")
input1=int(input("num1:"))
input2=int(input("num2:"))
opt=int(input("enter operator here:"))
num=cal(input1,input2,opt)
print(num)


