def dfs(node,parent):
    currsize=1
    for child in tree[node]:
        if child!=parent:
            currsize+=dfs(child,node)

    subsize[node]=currsize
    return currsize

n=int(input())
tree=[[]for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    tree[a].append(b)
    tree[b].append(a)

subsize=[0 for i in range(n)]
dfs(0,-1)
print(subsize)
