sen=input("Enter a string")
res=sen.split()
Biglen=0
for word in res:
    if len(word)>Biglen:
        Biglen=len(word)
        Bigword=word
    print("Biggest word lengthwise is",Bigword)
