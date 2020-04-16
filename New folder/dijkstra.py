from collections import defaultdict

import heapq

# initialisation

n = 5

graph = defaultdict(list)

dist = [float('inf')]*n

heap = []

# adding the following edges

edges = [(0, 1), (1, 2), (2, 4), (4, 3), (3, 0), (3, 1), (1, 4)]

weight = [6, 5, 5, 1, 1, 2, 2];

for i in range (0, len(edges)):

    x = edges[i][0]

    y = edges[i][1]

    w = weight[i];

    #Adding the weighted edges

    graph[x].append((w, y))

    graph[y].append((w, x))

 

src = 0

# add edge to heap with edge weight priority

heapq.heappush(heap, (0, src))

dist[0] = 0

 

while len(heap) > 0:

    # heap[0] gives the top element in the min heap

    node = heap[0][1]

    heapq.heappop(heap)

    for i in range(0, len(graph[node])):

        nextnode = graph[node][i][1]

        w = graph[node][i][0]

 

        if dist[nextnode] > dist[node] + w:

            dist[nextnode] = dist[node] + w;

            heapq.heappush(heap, (dist[nextnode], nextnode))

 

print("Shortest distance from source vertex " + str(src) + " to vertex")

for i in range(0,n):

    print(str(i) + ": " + str(dist[i]))