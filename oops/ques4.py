class Birds:
    def category(self):
        print("this is category of bird")
    def fly(self):
        print("I can fly")
class Sparrow(Birds):
    pass
class Crow(Birds):
    pass
class ostrich(Birds):
    def fly(self):
        print("I can't fly")

objBird=Birds()
objsparrow=Sparrow()
objCrow=Crow()
objostrich=ostrich()
objBird.category()
objBird.fly()
objsparrow.category()
objsparrow.fly()
objCrow.category()
objCrow.fly()
objostrich.category()
objostrich.fly()
