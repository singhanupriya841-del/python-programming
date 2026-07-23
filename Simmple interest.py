principal = int(input("Enter your Principal Amount Here"))
Rate = int(input("Enter your Rate OF Interest Here"))
Time = int(input("Enter your Time Period Here"))
SI = (principal*Rate*Time)/100
print("calculated Simple Interest :", SI)
Total_amount = int(principal + SI)
print('Total Amount on Maturity:',Total_amount)
