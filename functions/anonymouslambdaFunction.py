def name(x):
    return lambda a,b:a+x+b
num=name(10)
print(num(5,10))    