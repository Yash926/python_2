class Person:
    def __init__(self,Name,Age):
        self.__name=Name
        self.__age=Age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
Person1=Person("Yash",22)
# print(Person1.__name)
print(Person1._Person__name)

         