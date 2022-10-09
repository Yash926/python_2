#a company decided to give bonus of 1000Rs to
#employee if his/her dervice is more than 5 years
#ask user their salary and year of service and print
#the net bonus amount
year=float(input("how many years you have worked"))
salary=float(input("current salary you are getting"))
if year>5:
    print("you wil get a bonus of 1000rs")
    print("your salary after bonus:",salary+1000)
else:
    print("you are not eligible for bonus")    