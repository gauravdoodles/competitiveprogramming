from math import ceil,log
def levels(u,parent,level):
	Level[u]=level
	dp[u][0]=parent
	for v in tree[u]:
		if v!=parent:
			levels=(v,u,level+1)

def preprocess():
	levels(0,-1,0):
	for i in range(1,n):
		for u in range(n):
			v=dp[u][i-1]
			dp[u][i]=dp[v][i-1] if v!=-1 else:-1

def lca(u,v):
	if v=u:
		return u

	if Level[u]<Level[v]:
		return lca(v,u)
	i=ceil(log2(n))+1
	while Level[u]<level[v]:
		if dp[u][i]!=-1 and Level[dp[u][i]]>=Level[v]:
			u=dp[u][i]

		i=i-1