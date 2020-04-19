from math import gcd


class Edge:
    def __init__(self, u, v, weight1,weight2):
        self.u = u
        self.v = v
        self.weight1 = weight1
        self.weight2=weight2



class DisjointSet:
    def __init__(self, n):
        # Args:
        #   n (int): Number of vertices in the graph

        self.parent = [None] * n # Contains wich node is the parent of the node at poisition <i>
        self.size = [1] * n # Contains size of node at index <i>, used to optimize merge
        for i in range(n):
            self.parent[i] = i # Make all nodes his own parent, creating n sets.

    def merge_set(self, a, b):
        # Args:
        #   a, b (int): Indexes of nodes whose sets will be merged.

        # Get the set of nodes at position <a> and <b>
        # If <a> and <b> are the roots, this will be constant O(1)
        a = self.find_set(a)
        b = self.find_set(b)

        # Join the shortest node to the longest, minimizing tree size (faster find)
        if self.size[a] < self.size[b]:
            self.parent[a] = b # Merge set(a) and set(b)
            self.size[b] += self.size[a] # Add size of old set(a) to set(b)
        else:
            self.parent[b] = a # Merge set(b) and set(a)
            self.size[a] += self.size[b] # Add size of old set(b) to set(a)

    def find_set(self, a):
        if self.parent[a] != a: 
            # Very important, memoize result of the 
            # recursion in the list to optimize next
            # calls and make this operation practically constant, O(1)
            self.parent[a] = self.find_set(self.parent[a])

        # node <a> it's the set root, so we can return that index
        return self.parent[a]


def kruskal(n, edges, ds):
    # Args:
    #   n (int): Number of vertices in the graph
    #   edges (list of Edge): Edges of the graph
    #   ds (DisjointSet): DisjointSet of the vertices
    # Returns:
    #   int: sum of weights of the minnimum spanning tree 
    #
    # Kruskal algorithm:
    #   This algorithm will find the optimal graph with less edges and less
    #   total weight to connect all vertices (MST), the MST will always contain
    #   n-1 edges because it's the minimum required to connect n vertices.
    #
    # Procedure:
    #   Sort the edges (criteria: less weight).
    #   Only take edges of nodes in different sets.
    #   If we take a edge, we need to merge the sets to discard these.
    #   After repeat this until select n-1 edges, we will have the complete MST.
    edges.sort(key=lambda edge: edge.weight1/edge.weight2)
    edges=edges[::-1]
    mst = [] # List of edges taken, minimum spanning tree

    for edge in edges:
        set_u = ds.find_set(edge.u) # Set of the node <u>
        set_v = ds.find_set(edge.v) # Set of the node <v>
        if set_u != set_v:
            ds.merge_set(set_u, set_v)
            mst.append(edge)
            if len(mst) == n-1: 
                # If we have selected n-1 edges, all the other 
                # edges will be discarted, so, we can stop here
                break

    return [(int(edge.u),int(edge.v),float(edge.weight1),float(edge.weight2)) for edge in mst]





n,m=map(int,input().split())
ds=DisjointSet(m)

edges=[None]*m

for i in range(m):
		u,v,a,b=map(int,input().split())
		edges[i]=Edge(u,v,a,b)
		
cost1=0
cost2=0
mst=kruskal(n,edges,ds)
for i in range(len(mst)):
	cost1+=mst[i][2]
	cost2+=mst[i][3]
cost1=int(cost1)
cost2=int(cost2)
z=gcd(cost1,cost2)
cost1=int(cost1/z)
cost2=int(cost2/z)
print("{0}/{1}".format(cost1,cost2))
