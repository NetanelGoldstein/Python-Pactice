hrs = float(input('How many hours did you work this week?'))
rte = float(input('What is your rate of pay per hour?'))
def calpay()
    if hrs<=40.0:
    ttl=hrs*rte
    print(ttl)
    else:
     ot=hrs-40
     ttl=(ot*(rte*1.5))+(40*rte)
     print(ttl)
q=input('Press Enter to Close')
