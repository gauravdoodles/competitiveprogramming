

def dfs(root,parent):
    global timer
    flat[timer]=root
    timer+=1
    for child in tree[root]:
        if child!=parent:
            dfs(child,root)

    flat[timer]=root
    timer+=1

tree=[[] for i in range(4)]
for i in range(1,4):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
timer=1
flat=[0 for i in range(2*3+2)]
dfs(1,0)
print(flat)

