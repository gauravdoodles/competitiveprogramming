#owl fight hackerrank.com


# n=input()
n=5
parent=[-1 for i in range(n+1)]
rank=[1 for i in range(n+1)]
def find(a):
    if parent[a]<0:
        return a

    else:
        x=find(parent[a])
        parent[a]=x
        return x
        

def union(a,b):
    parent[a]=min(parent[a],parent[b])
    parent[b]=a

# original
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return 

    if rank[a]>rank[b]:
        parent[b]=a
        rank[a]+=rank[b]
    else:
        parent[a]=b
        rank[b]+=a


for i in range(3):
    a,b=map(int,input().split())
    union(a,b)

for q in range(2):
    x,y=map(int,input().split())
    if find(x)==find(y):
        print("TIE")
    if find(x)>find(y):
        print(x)
    if find(y)>find(x):
        print(y)



