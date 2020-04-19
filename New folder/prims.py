from collections import defaultdict

import heapq

# initialisation

graph = defaultdict(list)

visited = [0]*100

heap = []

n = 4

# adding the following edges

edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]

weight = [1, 4, 2, 6, 7, 5, 3];

for i in range (0, len(edges)):

    x = edges[i][0]

    y = edges[i][1]

    w = weight[i];

    #Adding the weighted edges

    graph[x].append((w,y))

    graph[y].append((w,x))

 

# start at an arbitrary node - here 0

# add edge to heap with edge weight priority

for i in range(0,len(graph[0])):

    heapq.heappush(heap,(graph[0][i],0))
print(heap)
visited[0] = 1

cost = 0

mst = []

# while there is an unvisited node

# here we consider that the given graph is connected

while len(mst) < n:

    # get minimum-weight edge to an unvisited node from heap

    # heap[0] gives the top element in the min heap with edge weight priority

    w = heap[0][0][0]

    previousnode = heap[0][1]

    node = heap[0][0][1]

    heapq.heappop(heap)

 

    # already visited 

    if visited[node] == 1:

        continue

 

    # found new reachable node. Mark visited and update MST        

    visited[node] = 1

    cost = cost + w

    mst.append((node, previousnode))

 

    # add all edges from this node to the heap

    for i in range(0, len(graph[node])):

        heapq.heappush(heap, (graph[node][i], node))

 

print("Minimum cost of spanning tree is: " + str(cost))

print("Following are the edges in MST: ")

for i in range(0,len(mst)):

    print(str(mst[i][0]) + " " + str(mst[i][1]))