#take input of age fron 3 person
#determine the oldest and youngest person
person1=int(input("age of first person:"))
person2=int(input("age of second person:"))
person3=int(input("age of third person:"))
#for oldest person
if person1>person2 and person1 >person3:
    print("person1 is oldest")
elif person2>person1 and person2>person3:
    print("person 2 is oldest")
elif person3>person2 and person3>person1:
    print("person 3 is oldest")   
#for youngest person
if person1<person2 and person1<person3:
    print("person 1 is younest") 
elif person2<person1 and person2<person3:
    print("person 2 is youngest")
elif person3<person2 and person3<person1:   
    print("person 3 is youngest")        
else: print("all have the same age")    