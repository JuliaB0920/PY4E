#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
#Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 43). Kindle Edition.
hrs = input("enter hours")
hrs = float(hrs)
rph = input("enter rate per hour")
rph = float(rph)
gross=hrs*rph
print("Pay:" , gross)
