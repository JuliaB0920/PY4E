fname = input("Enter file name: ")
fh = open(fname)
for l in fh:
    lx = l.rstrip()
    print(lx.upper())
