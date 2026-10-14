n=10
A=(0,1)
f=0
s=1
for i in range (0,n-2):
    T=f+s
    A=A+(T,)
    f=s
    s=T
print(A)
