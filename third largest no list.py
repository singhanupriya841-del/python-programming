l = [12, 5, 11, 16, 6, 4, 13, 21]
largest = 0
seclarge = 0
thirdlarge = 0
for i in l:
    if i > largest:
        thirdlarge = seclarge
        seclarge = largest
        largest = i
    elif i > seclarge:
        thirdlarge = seclarge
        seclarge = i
    elif i > thirdlarge:
        thirdlarge = i
print("third largest no is", thirdlarge)
