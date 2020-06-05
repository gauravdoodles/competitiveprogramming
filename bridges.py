def dfs(node,par):
    vis[node]=1
    In[node]=low[node]=timer 
    timer+=1
    for child in graph[node]:
        if child==par:
            continue
        if vis[child]==1:
            low[node]=min(low[node], In[child])
        else:
            dfs(child,node)

            if low[child]>In[node]:
                print("{0} -> {1} is a bridge".format(child,node))
                low[node]=min(low[node], low[child])


    