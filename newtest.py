n,m=map(int,input().split())
arr=[[]for i in range(n)]
for i in range(n):
	a,b,c=map(int,input().split())
	a,b,c=a-1,b-1,c-1

	arr[a].append([b,c])
arr=sorted(arr,key=lambda x:x[2])
let=len(arr)
for i in range(1,n):
	if 