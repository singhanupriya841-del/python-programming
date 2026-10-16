T=((2,5),(4,2),(9,8),(12,10))
count=0
for i in T:
    if i[0]%2==0 and i[1]%2==0:
        count+=1
print("No.of even pairs is",count)
      
