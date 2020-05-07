
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class DisjointSet:
    def __init__(self, n):

        self.parent = [None] * n
        self.size = [1] * n
        for i in range(n):
            self.parent[i] = i

    def merge_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)

        if self.size[a] < self.size[b]:
            self.parent[a] = b
            self.size[b] += self.size[a]
        else:
            self.parent[b] = a
            self.size[a] += self.size[b]

    def find_set(self, a):
        if self.parent[a] != a:

            self.parent[a] = self.find_set(self.parent[a])

        return self.parent[a]


def kruskal(n, edges, ds):

    edges.sort(key=lambda edge: edge.weight)
    
    mst = []
    for edge in edges:
        set_u = ds.find_set(edge.u)
        set_v = ds.find_set(edge.v)
        if set_u != set_v :
            ds.merge_set(set_u, set_v)
            mst.append(edge)

            if len(mst) == n-1:

                break

    return sum([edge.weight for edge in mst])


if __name__ == '__main__':
    for _ in range(int(input())):
        n, m = map(int, input().split())
        doodhwala = list(map(int, input().split()))
        edges = []

        ds = DisjointSet(m)
        for z in range(m):
            u, v, weight = map(int, input().split())
            u = u-1
            v = v-1
            if doodhwala[u]==1:
                edges.append(Edge(n,u,0))
            elif doodhwala[v]==1:
                edges.append(Edge(n,v,0))
            else:
                edges.append(Edge(u, v, weight))
        print(edges)
        ans = kruskal(n, edges, ds)
        print(ans)
