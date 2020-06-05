def dfs(node,parent):
    for child in graph[node]:
        if child!=parent:
            dfs(child,node)
    taken,nottaken=1,0
    for neigh in graph[node]:
        if neigh!=parent:
            taken+=dp[neigh][0]
            nottaken+=dp[neigh][1]
    dp[node][1]=min(taken,nottaken)
    dp[node][0]=nottaken


if __name__ == '__main__':

    n=int(input())
    dp=[[0 for j in range(2)] for i in range(n)]
    graph=[[]for i in range(n)]
    for i in range(n-1):
        a,b=map(int,input().split())
        a=a-1
        b=b-1
        graph[a].append(b)
        graph[b].append(a)
    dfs(0,-1)
    print(dp)