

from sys import stdin,stdout



def bs(start,end,key):
	while(start<end):
		mid=(start+end)//2
		if key>=arr[mid][0]:
			start=start+1
		else:
			end=mid
	return start


for _ in range(int(stdin.readline())):
	arr=[]
	n=int(stdin.readline())
	for i in range(n):
		a,b,c=map(int,stdin.readline().split())
		b=a+b
		arr.append([a,b,c])

	arr.sort()
	presum=[0 for i in range(n)]
	presum[0]=arr[0][2]
	for i in range(1,n):
		presum[i]=presum[i-1]+arr[i][2]

	bada_ans=0
	
	for i in range(n):
		chota_ans=arr[i][2]
		idx=bs(0,n,arr[i][1])
		chota_ans+=presum[n-1]-presum[idx-1]
		bada_ans=max(bada_ans,chota_ans)

	stdout.write(str(bada_ans))





	
