#create a function that will display the how many items in the list have
#names more than 5 characters
#names=["Atul","shubham","Anurag","rahul","Dev,"Roy"]
listOfName=["Atul","shubham","Anurag","rahul","Dev","Roy"]
def count(listOfName):
    count=0
    for i in listOfName:
        if len(i)>5:
            count+=1
    return count
print(count(listOfName))    
            
            