from collections import deque
#0 based indexing
def kahn(n):
    q=deque()
    for i in range(n):
        if In[i]==0:
            q.append(i)
    while len(q)!=0:
        curr=q.popleft()
        res.append(curr)

        for node in graph[curr]:
            In[node]=In[node]-1
            if In[node]==0:
                q.append(node)



if __name__=="__main__":
    n,e=map(int,input().split())
    graph=[[] for i in range(n)]
    In=[0 for i in range(n)]
    res=[]
    for i in range(e):
        a,b=map(int,input().split())
        graph[a].append(b)
        In[b]+=1

    kahn(n)
    print(res)




