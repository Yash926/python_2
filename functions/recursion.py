# import sys 
# sys.setrecursionlimit(2000)
# print()
# def hello():
#     print("hello world")
#     hello()
# hello()
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
num=fact(4)
print(num)    