n=int(input())
arr=list(map(int,input().split()))
dp=[0 for i in range(n)]
length=0
for i in range(n):
	for j in range(n):
		if abs(arr[j])<abs(arr[i])and arr[i]*arr[j]<0:
			length=max(length,dp[j])
		dp[i]=length+1
print(dp[n])