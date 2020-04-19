def dfs(x:int,parent:int):
	for y in graph[x]:
		if y==parent:
			continue
		dfs(y,x)

	taking,nottaking=v[x],0

	for y in graph[x]:
		if y==parent:
			continue
		taking+=dp[y][1]
		nottaking+=dp[y][0]
	dp[x][1]=nottaking
	dp[x][False]=max(taking,nottaking)

if __name__ == '__main__':
	n=int(input())
	v=list(map(int,input().split()))
	dp=[[0 for j in range(2)] for i in range(n)]
	graph=[[]for i in range(n)]
	for i in range(n-1):
		a,b=map(int,input().split())
		a=a-1
		b=b-1
		graph[a].append(b)

	dfs(0,-1)
	print(dp[0][0])