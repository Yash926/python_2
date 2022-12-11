#key and value pairs are must
# dictionary are ordered
#duplictaes are not allowed and also mutable
myDictionary={
"Name":"Yash",
"age":19
}
print(myDictionary)
myDict={
    "Name":"Yash",
    "age":19,
    "class":"B.Tech",
    "percentage":97.2
}
print(myDict)
print(len(myDict))
a=myDict.get("Name")        #to get access to a particular key value
b=myDict["Name"]
print(a)
print(b)
c=myDict.keys()     #to get keys
print(c)
d=myDict.values()       #to get values
print(d)
e=myDict.items()      #to get items of a dictionary as list of tuples
print(e)
myDict["age"]=22            #to change particular value
print(myDict)
myDict.update({"age":22})       #update method to change particular value
print(myDict)
myDict.pop("class")
print(myDict)