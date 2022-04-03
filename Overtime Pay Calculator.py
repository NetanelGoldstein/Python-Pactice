hrs = input('How many hours did you work this week?')
try:
    hrs=float(hrs)
except:
    hrs=input('Please type digits')
    hrs=float(hrs)
rte = input('What is your rate of pay per hour?')
try:
    rte=float(rte)
except:
    rte=input('Please type digits')
    rte=float(rte)
if hrs<=40.0:
    ttl=hrs*rte
    print(ttl)
else:
     ot=hrs-40
     ttl=(ot*(rte*1.5))+(40*rte)
     print(ttl)
q=input('Press Enter to Close')
