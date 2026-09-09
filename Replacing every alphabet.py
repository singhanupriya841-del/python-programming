a="Welcome all"
res=''
for i in range (0,len(a)):
    if i%2==0:
        res=res+a[i].upper()
    else:
        res=res+a[i]
print(res)
