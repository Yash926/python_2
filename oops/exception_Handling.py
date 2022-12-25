#try:
    #this block of code will run and throw errrors if there are any

#except:
        #this will raise the errors

#else:
        #this will execute if there are no errors
#finally:
    #THIS WILL execute regardless the result of try and except

# try:
#     f = open("chapter5.txt")
#     try:
#         f.write("ABC")
#     except:
#         print("Error in file")
#     finally:
#         f.close()
# except:
#     print("can't open the file")

a=5
if a<10:
    raise Exception("Value is less than 5")
