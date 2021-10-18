min = None
max = None
while True :
    sval = input('Enter a number:')
    if sval == 'done' :
        break
    try:
        ival = int(sval)
    except:
        print('Invalid input')
        continue

    if min is None :
        min = ival
    elif min > ival :
        min = ival
    if max is None :
        max = ival
    elif max < ival :
        max = ival


print('Maximum is' , max)
print('Minimum is' , min)
