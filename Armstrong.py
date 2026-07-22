n=int(input("Enter a number"))
count=0
num=n
while n>0:
    n=n//10
    count=count+1
n=num
ren=0
while n>0:
    r=n%10
    ren=ren+(r** count)
    n=n//10
if ren==num:
    print(ren, "15 armstrongnum")
else:
    print('not armstrong')
    
