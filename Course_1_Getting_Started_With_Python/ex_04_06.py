h = input("Enter hours:")
h = float(h)
r = input("Enter rate:")
r = float(r)
def computepay(h,r) :
    overtime = 40*r + (h-40)*(1.5*r)
    pay = r*h
    if h > 40 :
        return(overtime)
    else :
        return(pay)
p = computepay(h,r)
print("Pay" , p)
