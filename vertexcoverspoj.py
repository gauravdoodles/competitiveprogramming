def dfs(node,parent,ptaken):
	if dp[node][ptaken]!=-1:
		return dp[node][ptaken]
	taking,nottaking=1,0
	total=0
	tways
	for neig in graph[node]:
		if neig!=parent:
			taking+=dfs(neig,node,1)
			nottaking+=dfs(neig,node,0)

	if ptaken:
		dp[node][ptaken]=min(taking,nottaking)
	else:
		dp[node][ptaken]=taking
	return dp[node][ptaken]




if __name__ == '__main__':
	n=int(input())
	graph=[[]for ii in range(n)]
	for i in range(n-1):
		a,b=map(int,input().split())
		a=a-1
		b=b-1
		graph[a].append(b)
		graph[b].append(a)
	

	dp=[[-1 for i in range(2)]for j in range(n)]
	print(dfs(0,-1,1))
	

