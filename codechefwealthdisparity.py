arr=list(map(int,input().split()))
n=arr[0]
graph=[[]for i in range(n+1)]
cost=[]
for i in range(1,n+1):
	cost.append(arr[i])
cost=[0]+cost
manager=[]
for i in range(n+1,2*n+1):
	manager.append(arr[i])
manager=[0]+manager
for i in range(1,n+1):
	k=manager[i]
	if manager[i]!=-1:
		graph[k].append(i)


idx=manager.index(-1)

max1=0
zx=idx
zy=-1
for i in range(1,n+1):
	zz=cost[idx]
	if manager[i]!=-1:
		zz=zz-cost[i]
		if zz>max1:
			zy=i
			max1=zz
		
for i in range(1,n+1):
	if i!=idx:
		for k in graph[i]:
			newcost=cost[i]-cost[k]
			if newcost>max1:
				zx=i
				zy=k
				max1=newcost


print(max1)