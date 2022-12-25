                #file handling

#f = open("chapter5.txt","r")# r- read mode denotes read mode and w denotes  writing
# # # print(f.read())
# # print(f.readline())
# # print(f.readline())

# #how towrite a file
# f1 = open("demo1.text","w")
# f1.write("this is a new file\n")

# f2=open("demo2.txt", "w")  w-file can also be written
# f2.write("My name is Yash tripathi") 
# f2.write("\nI am student at lovely Professional University\n")


# for i in f:
#     f1.write(i)
# try:
#     f=open("demo1.txt")
#     #your code goes here
# finally:
#     f.close()
#this way we are making sure that file is closed properly
# even if exception is raised  that acuse the program  flow to stop
#with open("demo1.txt") as f:
    #f.read() #--> example
    #your code goes here
# f=open("demo1.txt", "r")
# print(f.read(10))
# print(f.tell())

# f = open("img.jpg",'rb') #in case of image file we use rb, it prints the binary of image
# # copy = f.read()
# f1 = open("img_copy.jpg","wb")
# # f1.write(copy)
# # f1.close()
# for i in f:
#     f1.write(i)

import os
# os.remove("demo1.txt")
if os.path.exists("demo1.txt"):
    os.remove("demo1.txt")
else:
    print("File does not exist")
