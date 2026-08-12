x=int(input('enter a value of x:'))
n=int(input('enter a value of n:'))
SUM=0
for i in range(0,n+1):
    SUM=SUM+(x**i)
print('sum of the series is',SUM)
