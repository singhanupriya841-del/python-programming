x=int(input('enter a value of x:'))
n=int(input('enter a value of n:'))
fact=1
SUM=0
for i in range(1,n+1):
    fact=fact*i
    SUM=SUM+(x**i)/fact
print("Sum of the series is",SUM)
