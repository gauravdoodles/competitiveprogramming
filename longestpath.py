n=int(input())
tree=[[] for i in range(n)]
visited=[0 for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a=a-1
    b=b-1
    tree[a].append(b)
    tree[b].append(a)
maxnode=None
maxd=-1
def dfs(node,d):
    global maxnode,maxd
    visited[node]=1
    if d>maxd:
        maxd,maxnode=d,node

    for child in tree[node]:
        if visited[child]==0:
            dfs(child,d+1)

dfs(0,0)
visited=[0 for i in range(n)]
maxd=-1
dfs(maxnode,0)
print(maxd)



