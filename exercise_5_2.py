largest = None
smallest = None
while True:
    sval = input('Enter a Number')
    if sval == 'done':
        break
    try:
        ival = int(sval)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = ival
    if smallest == None:
        smallest = ival
    if ival > largest:
        largest = ival
    if ival < smallest:
        smallest = ival
print('Maximum is',largest)
print('Minimum is', smallest)
