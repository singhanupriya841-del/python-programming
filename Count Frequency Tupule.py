T=(1,2,3,8,3,4,5,3,8,2,4,1)
s=[]
for i in T:
    if i not in s:
        print('frequency of',i,'is',T.count(i))
        s.append(i)
