a=input("Enter any sentence")
vow=0
up=0
low=0
dig=0
sp=0
for i in a:
    if i in 'AEIOUaeiou':
        vow+=1
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1
    elif i.isdigit():
        dig+=1
    elif i.isspace():
        sp+=1
print("No.of vowels",vow)
print("No of up",up)
print("No of low",low)
print("No of dig",dig)
print("No of sp",sp)
