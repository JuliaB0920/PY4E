#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method.
#Compute the average of the numbers and print out the average. Enter file:mbox.txt

#Severance, Charles. Python for Everybody: Exploring Data in Python 3 (p. 191). Kindle Edition.

import re
file = input("Enter file name:")
handle = open(file)
newrevlist = list()
for line in handle :
    lines = line.rstrip()
    newrev = re.findall('^New.Revision:.([0-9.]+)', lines)
    if len(newrev) != 1 : continue
    newrevnum = float(newrev[0])
    newrevlist.append(newrevnum)
print((sum(newrevlist)/len(newrevlist)))
