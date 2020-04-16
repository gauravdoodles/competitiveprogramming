n,m=map(int,input().split())

graph=[[]for i in range(n)]
for i in range(m):
	a,b=map(int,input().split())
	a=a-1
	b=b-1
	graph[a].append(b)
	graph[b].append(a)
	
visited=[0 for i in range(n)]
tree=True
def dfs(src,par):
	visited[src]=1

	for child in graph[src]:
		if visited[child]==0:

			dfs(child,src)
		elif child!=par:
			tree=False
	return

ans=0
for src in range(n):
	if visited[src]==0:
		if  dfs(src,-1):
			ans=ans+1

print(ans)


