#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address
#to a count of the number of times they appear in the file.
#After the dictionary is produced,
#the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
handle = open(name)

emailtot = dict()
emaillist = list()
for line in handle :
    if not line.startswith("From ") : continue
    emailline = line.split()
    emaillist.append(emailline[1])
#This is the less precise way of adding things to the dictionary
#for email in emaillist :
    #if email not in emailtot :
        #emailtot[email] = 1
    #else :
        #emailtot[email] = emailtot[email] + 1
#This way is better:
for email in emaillist :
    emailtot[email] = emailtot.get(email, 0) + 1

commonemail = None
commoncount = None
for email, count in emailtot.items() :
    if commoncount is None or count > commoncount :
        commonemail = email
        commoncount = count

print(commonemail, commoncount)
