def dfs(node, parent, ptaken):
    if dp[node][ptaken] != -1:
        return dp[node][ptaken]
    taking, nottaking = 1, 0
    total = 0
    tways=1
    nways=1
    ways[node][ptaken]=1
    for neig in graph[node]:
        if neig != parent:
            taking += dfs(neig, node, 1)
            nottaking += dfs(neig, node, 0)
            tways=(tways*ways[neig][1])%10007
            nways=(nways*ways[neig][0])%10007



    if ptaken:
        dp[node][ptaken] = min(taking, nottaking)
        if taking==nottaking:
        	ways[node][ptaken]=(tways+nways)%10007
        elif taking<nottaking:
        	ways[node][ptaken]=tways
        else:
        	ways[node][ptaken]=nways
    else:
        dp[node][ptaken] = taking
        ways[node][ptaken]=tways

    return dp[node][ptaken]


if __name__ == '__main__':
    for _ in range(int(input())):
    	n = int(input())
    	graph = [[]for ii in range(n)]
    	for i in range(n - 1):
    	    a, b = map(int, input().split())
    	    a = a - 1
    	    b = b - 1
    	    graph[a].append(b)
    	    graph[b].append(a)

    	dp = [[-1 for i in range(2)]for j in range(n)]
    	ways=[[0 for i in range(2)]for j in range(n)]
    	a=dfs(0, -1, 1)
    	b=ways[0][1]
    	print(str(a)+" "+str(b))
