Data={}
ch='yes'
while ch=='yes':
    team=input("Enter team name")
    wins=int(input("Enter no of wins"))
    loss=int(input("Enter no of losses"))
    mdata=[wins,loss]
    Data[team]=mdata
    ch=input("want to enter more teams data enter yes/no")
teamname=input("Enter team name to print winning percentage")
if teamname in Data:
    winpercentage=(Data[teamname][0]/sum(Data[teamname]))*100
    print("winning percentage of",teamname,"is",winpercentage)
else:
    print("team does not exists")
