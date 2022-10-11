p=int(input("Enter principal amount here:"))
r=int(input("enter rate of interest here:"))
t=int(input("enter time here:"))
A=p*(1+(r/100))**t
ci=A-p
print("compound interest is:",ci)