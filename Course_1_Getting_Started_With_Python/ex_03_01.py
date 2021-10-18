#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
#Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 59). Kindle Edition.
hrs = input("Enter hours:")
hrs = float(hrs)
rate = input("Enter rate:")
rate = float(rate)
overtime = 40*rate + (hrs-40)*(1.5*rate)
pay = rate*hrs
if hrs > 40 :
    print(overtime)
else :
    print(pay)
