def floyd_warshall(graph, v,z,src,dest):


    dist = [[float("inf") for _ in range(v)] for _ in range(v)]

    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]

           
    for k in range(z):
       
        for i in range(v):
            
            for j in range(v):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]


    return dist[src][dest]












for _ in range(int(input())):
	n=int(input())
	graph=[[0 for i in range(n)]for j in range(n)]
	for i in range(n):
		for j in range(i,n):
			graph[i][j]=int(input())

	p=int(input())
	ids=[map(int,input().split())]
	q=int(input())
	for i in range(q):
		k,src,dest=map(int,input().split())
		src=src-1
		dest=dest-1
		print(floyd_warshall(graph,n,k,src,dest))