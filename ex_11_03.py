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
