n=int(input("Enter a number of students"))
d={}
for i in range(0,n):
    dnew={}
    a=int(input("Enter roll no."))
    b=input("Enter a name")
    c=int(input("Enter percentage"))
    dnew["name"]=b
    dnew["per"]=c
    d[a]=dnew
print(d)
