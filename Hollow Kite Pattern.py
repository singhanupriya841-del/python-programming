n=int(input("Enter first row"))
for i in range(0,n):
    for j in range(0,i+1):
        if j==0 or j==i:
         print('*',end='')
        else:
            print(' ',end='')
    for j in range(0,2*(n-i)-2):
     print(' ',end='')
    for j in range(0,i+1):
     if j==0 or j==i:
         print('*',end='')
     else:
        print(' ',end='')
    print()
for i in range(1,n):
    for j in range(0,n-i):
        if j==0 or j==n-i-1:
         print('*',end='')
        else:
            print(' ',end='')
    for j in range(0,2*i):
        print(' ',end='')
    for j in range(0,n-i):
        if j==0 or j==n-i-1:
         print('*',end='')
        else:
            print(' ',end='')
    print()
