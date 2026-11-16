D={'Jan':31,'Feb':28,'Mar':31,'April':30,'May':31,'June':30,'July':31,'August':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
Data=[]
for i in D:
    Data.append([D[i],i])
Data.sort()
Dnew={}
for i in Data:
    Dnew[i[1]]=i[0]
print("Dictionary sorted by no.of days in month",Dnew)
