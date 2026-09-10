a=input("Enter a line of text")
count=0
res=a.split()
for word in res:
    vcount=0
    for letter in word:
        if letter in "aeiouAEIOU":
           vcount+=1
    if vcount>=2:
            count+=1
            print(word)
            
