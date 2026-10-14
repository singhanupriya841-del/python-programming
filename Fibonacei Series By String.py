n=10
L=[0,1]
f=0
s=1
for i in range (0,n-2):
    T=f+s
    L.append(T)
    f=s
    s=T
 print(L)
    
    
