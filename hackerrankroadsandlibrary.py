for _ in range(int(input())):
    n,m,lib,road=map(int,input().split())
    graph =[[]for i in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        a=a-1
        b=b-1
        graph[a].append(b)
        graph[b].append(a)
    count=[0 for i in range(n)]
    visited=[0 for i in range(n)]
    countroad=0
    def  dfs(src):
        global countroad
        visited[src]=1
        
        for child in graph[src]:
            if visited[child]==0:
                countroad+=1
                dfs(child)
    count=0
    for i in range(n):
        if visited[i]==0:
            count+=1
            dfs(i)
    chuchi=0
    if lib<=road:
        print(n*lib)
    else:
        chuchi=lib*count+countroad*road
        print(chuchi)


