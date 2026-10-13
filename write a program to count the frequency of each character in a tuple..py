T=(1,2,3,8,3,4,5,3,8,2,4,1)
S=[]
for i in T:
    if i not in S:
        print('frequency',i,'is',T.count(i))
        S.append(i)
