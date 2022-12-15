#instance methods-methods dependent on the object we make.
class student:
    numberOfSubjects=5              #class objects
    def __init__(self,marks1,marks2,marks3):
        self.web=marks1
        self.python=marks2
        self.math=marks3
    def average(self):
        print("Averge marks are : ",(self.web+self.python+self.math)/3)
    # def getmarks(self):
    #     return self.math            #accesssors

    # def setmarks(self,marks):
    #     self.math=marks                 #Mutators   
    
    @classmethod
    def classMethodsExample(cls):
        return cls.numberOfSubjects
    
    @staticmethod
    def staticmethod():
        print("This is an example of static method")
student1=student(5,4,3)
student2=student(7,8,9)
student3=student(9,8,7)
student1.average()
student2.average()
student3.average()
print(student.classMethodsExample())
student.staticmethod()