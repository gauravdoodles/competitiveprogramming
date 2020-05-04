n,m=map(int,input().split())
arr=list(map(int,input().split()))
newarr=[]
for i in range(n):
	arr.append((arr[i],i))
newarr.sort()
pos=[0 for i in range(n)]
for i in range(n):
	pos(newarr[i][1])=i

