num=[4,5,1,3,8,7]
denum=[3,2,2,1,5,3]
small=num[0]/denum[0]
for i in range(0,len(num)):
    fr=num[i]/denum[i]
    if fr<small:
        small=fr
print("Smallest fraction of the list is",small)
