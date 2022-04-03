tot = 0
count = 0
while True:
    sval = input('Enter Number. Type done when done. ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('please enter numbers only')
        continue
    tot = fval+tot
    count = count+1
print('Sum', tot, 'Count', count, 'Average', tot/count)
