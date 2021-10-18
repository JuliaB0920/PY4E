#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
#Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 59). Kindle Edition.
hrs = input("Enter hours:")
rate = input("Enter rate:")
try:
    hrs = float(hrs)
    rate = float(rate)
except:
    hrs = -1
    rate = -1
    if hrs < 0 :
        print("Please enter a valid numerical value.")
        quit()
    if rate < 0 :
        print("Please enter a valid numerical value.")
        quit()
overtime = 40*rate + (hrs-40)*(1.5*rate)
pay = rate*hrs
if hrs > 40 :
    print(overtime)
else :
    print(pay)
