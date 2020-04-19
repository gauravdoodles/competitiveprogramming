
vertices=4

p=[None for v in range(vertices)]
rank=[0 for v in range(vertices)]
def create_set(x):
	p[x]=x
	rank[x]=0
def merge_sets(x,y):
	px=find_set(x)
	py=find_set(y)
	if rank[px]>rank[py]:
		p[py]=px
	else:
		p[px]=py

	if rank[px]==rank[py]:
		rank[py]=rank[py]+1
def find_set(x):
	if x!=p[x]:
		find_set(p[x])
	return p[x]

for i in range(4):
	create_set(i)

merge_sets(1,2)
print(find_set(2))

