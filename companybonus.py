# companu will give bonus based on following criteria
#time spent in company              Bonus
#>10years                            10%
#>6 and <10                          8%
#less than 6                         5%
#ask salary and time spent from the user
#print net bonus amount accordingly
currentSalary=float(input("enter your salary here:"))
timeSpent=float(input("enter time spent in the company:"))

if timeSpent>=10:
    print("your net bonus is:",currentSalary*0.1)
elif timeSpent>=6 and timeSpent<10:
    print("your net bonus is",currentSalary*0.08)
elif timeSpent<6:
    print("your net bonus is",currentSalary*0.05)
