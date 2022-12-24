a="hello"
b=[1,2,3,4,5,6]
print(len(b)) #if a function is working for different type of data then it is known as poly morphism


def add(a,b,c=0):
    return a+b+c
print(add(1,2))             #Method overlading : method having same name but no.of arguments are different 
print(add(1,2,3))


# method overloading concept
class Rect:
    def calculateArea(self,length=None,breadth=None):
        if length!=None and breadth!=None:
            return length*breadth
        elif length!=None:
            return length*length
rectangle=Rect()
print(rectangle.calculateArea(2,3))
print(rectangle.calculateArea(2))