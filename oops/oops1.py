a="5"
print(type(a))
class laptop:
    # in int method is is only defined doesn't needs calling
    def __init__(self,name,processor):
        self.name=name
        self.processor=processor
    def printOutput(self):
        print("My laptop name is : ", self.name, "and the processor is : ", self.processor)
    
#     def config(self):
#         print("HP","i7","1tb","16gb")
laptop1=laptop("hp","i7")
laptop2=laptop("asus","i9")
# # print(id(laptop1))
# # print(id(laptop2))

# # laptop.config()
# laptop1.config()
# laptop2.config()
laptop1.printOutput()
laptop2.printOutput()