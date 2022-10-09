total_lectures=int(input("enter total lectures:"))
lectures_attended=int(input("how many lectures attended:"))
attendance=(lectures_attended/total_lectures)*100
print("the percentage of your attendance is:",attendance,"%")
if attendance >= 75:
    print("you are eligible for exams")
else:
    print("you are not eligible for exams")    