#Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter file name: ")
fh = open(fname)
conf = 0
line_num = 0
for line in fh :
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cpos = line.find(":")
    line = line[cpos+1:]
    line = float(line.strip())
    conf = conf + line
    line_num = line_num + 1
average = conf/line_num
print("Average spam confidence:" , average)
