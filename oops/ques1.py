# class person:
#     def __init__(self,name,rollno):
#        self.name=name
#        self.rollno=rollno

#     def printOutput(self):
#         print("Name of the student is "+self.name+" Roll no is " ,self.rollno)
# person1=person("yash","47")
# person2=person("ayush","75")
# person1.printOutput()
# person2.printOutput()
class Person:
    def __init__(self):             #it is constructor it doesn't needs calling
        self.name="yash"             #these are called instance variable
        self.age=18
    def updateName(self):
        self.name="Ayush"
    def compareAge(self,other):
        if self.age==other.age:
            return True
        else:
            return False
    
person1=Person()
person2=Person()
person2.age=20
person1.updateName()
person2.name="onkar"
if person1.compareAge(person2):
    print("they are of same age")
else:
    print("they are of differnt age")

print(person1.name,person1.age)
print(person2.name,person2.age)




