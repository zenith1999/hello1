name=["Ram Singh"]
id=["RS009"]
drivingL=["123009"]
taxiNum=["CHD1720"]
kmtoGo=int(input("Enter distance to destination in KMs "))
print("name: ",name,"id: ",id,"drivingL: ",drivingL,"taxiNum: ",taxiNum)
basePrice=1000
if kmtoGo<=10:
    fare=basePrice+(kmtoGo*15)
elif kmtoGo>10 and kmtoGo<=50:
    fare=basePrice+(10*15)+((kmtoGo-10)*14)
elif kmtoGo>50 and kmtoGo<=200:
    fare=basePrice+(10*15)+(40*14)+((kmtoGo-50)*12)
elif kmtoGo>200 and kmtoGo<=500:
    fare=basePrice +(10*15)+(40*14)+(150*12)+(kmtoGo-200)*10
elif kmtoGo>500:
    fare=basePrice +(10*15)+(40*14)+(150*12)+(300*10)+((kmtoGo-500)*10)

total=(0.23*fare)+fare

print("total fare is: \n")
print(total)
