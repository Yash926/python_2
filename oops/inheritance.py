#capability of one class to inherit or derive properties from another class
#multi level  and multilevel inheritance
# class A:
#     def method1(self):
#         print("This is method1")
# a:class B():
#     def method2(self):
#         print("This is method 2")
# class B(A):# A is parent class and Bis child class
#     def method2(self):
#         print("This is method 2")
# class C(B):
#      def method3(self):
#         print("This is method 3 ")
# a:class C(B,A):
#     def method3(self):
#         print("This is method 3 ")

# objA=A()
# objB=B()
# objC=C()
# objC.method2() #B is child of A
class A:
    def __init__(self):
        print("This is init of Method A")
    def method1(self):
        print("This is method 2")
class B(A):
    def __init__(self):
        super().__init__()
        print("this is init of method B")
    def method2(self):
        print("This is method 2")
Obj1 = B()