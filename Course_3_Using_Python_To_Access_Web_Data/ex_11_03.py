#Finding Numbers in a Haystack

#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.

#Data Files
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_38794.txt (There are 90 values and the sum ends with 360)

#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+'
#and then converting the extracted strings to integers and summing up the integers.

import re
file = input("Enter file:")
handle = open(file)
filestring = handle.read()
def getnumbers(str) :
    array = re.findall('[0-9]+', str)
    array = [int(x) for x in array]
    return sum(array)
array = getnumbers(filestring)
print(array)
