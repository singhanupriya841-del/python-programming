l=[12,5,11,16,6,4,13,21]
largest=0
seclarge=0
for i in l:
    if i> largest:
        seclarge=largest
        largest=i
    elif i> seclarge:
        seclarge=i
print("second largest no is", seclarge)
