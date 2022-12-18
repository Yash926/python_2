#make a class car and 2 car class and one  bus class
#in car make a seating capacity 4 and override in bus
class vehicles:
    def seatingCapacity(self):
        print("The seating capacity is 4")
class car1(vehicles):
    pass
class car2(vehicles):
    pass
class bus(vehicles):
    def seatingCapacity(self):
        print("The seating capacity is 40")
objcar1=car1()
objcar2=car2()
objbus=bus()
objcar1.seatingCapacity()
objcar2.seatingCapacity()
objbus.seatingCapacity()
