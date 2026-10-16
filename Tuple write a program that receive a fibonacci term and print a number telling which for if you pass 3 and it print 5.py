n=int(input("Enter fibonacci term between 0 to 100"))
if n==0:
    print("it is",1,"fibonacci term")
elif n==1:
    print("it is",2,3,"fibonacci term")
else:
    f=0
    s=1
    term=3
    for i in range(0,97):
        t=f+s
        if t==n:
            print(")t is",term,"fibonacci term")
            term+=1
            break
        f=s
        s=t
        term=term+1
        
        
